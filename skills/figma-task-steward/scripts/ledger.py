"""Atomic compare-and-swap ledger for cooperating local Codex chats."""

import argparse
import contextlib
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile


STATUSES = {
    "dispatching", "pending", "clarifying", "awaiting_plan", "ready",
    "running", "blocked", "done", "cancelled",
}


def initial_state():
    return {
        "revision": 0, "surveyed": False, "manager": None,
        "workspace": {"owner_task": None, "borrower_task": None}, "tasks": {},
    }


def validate(state):
    if not isinstance(state, dict):
        raise ValueError("State must be an object")
    if type(state.get("revision")) is not int or state["revision"] < 0:
        raise ValueError("revision must be a nonnegative integer")
    if type(state.get("surveyed")) is not bool:
        raise ValueError("surveyed must be boolean")
    manager = state.get("manager")
    if manager is not None and (
        not isinstance(manager, dict) or not isinstance(manager.get("thread_id"), str)
        or not manager["thread_id"].strip()
    ):
        raise ValueError("manager needs a real thread_id")
    tasks = state.get("tasks")
    if not isinstance(tasks, dict):
        raise ValueError("tasks must be an object")
    threads = set()
    for key, task in tasks.items():
        if not key or not isinstance(task, dict) or task.get("status") not in STATUSES:
            raise ValueError("Invalid task key or status")
        for field in ("title", "node_url", "dispatch_token"):
            if not isinstance(task.get(field), str) or not task[field].strip():
                raise ValueError(f"Task {key} missing {field}")
        thread = task.get("thread_id")
        if thread is not None:
            if not isinstance(thread, str) or not thread.strip() or thread in threads:
                raise ValueError("Task thread IDs must be nonempty and unique")
            threads.add(thread)
    workspace = state.get("workspace")
    if not isinstance(workspace, dict) or set(workspace) != {"owner_task", "borrower_task"}:
        raise ValueError("workspace needs owner_task and borrower_task")
    owner, borrower = workspace["owner_task"], workspace["borrower_task"]
    for key in (owner, borrower):
        if key is not None and (
            not isinstance(key, str) or key not in tasks or not tasks[key].get("thread_id")
            or tasks[key]["status"] in {"dispatching", "done", "cancelled"}
        ):
            raise ValueError("Workspace holder must be a bound unfinished task")
    if owner is not None and not state["surveyed"]:
        raise ValueError("Survey existing workspace users before granting ownership")
    if borrower is not None and (
        owner is None or borrower == owner
        or tasks[borrower]["status"] not in {"clarifying", "awaiting_plan"}
    ):
        raise ValueError("Borrowing requires a different owner and a clarification task")


def read_state(path):
    if not path.exists():
        return initial_state()
    state = json.loads(path.read_text(encoding="utf-8"))
    validate(state)
    return state


@contextlib.contextmanager
def process_lock(path):
    # This short OS lock ends on process exit. Durable ownership stays in JSON.
    with path.open("a+b") as handle:
        handle.seek(0, os.SEEK_END)
        if handle.tell() == 0:
            handle.write(b"\0")
            handle.flush()
        handle.seek(0)
        if os.name == "nt":
            import msvcrt
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            yield
        finally:
            handle.seek(0)
            if os.name == "nt":
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def atomic_write(path, state):
    descriptor, filename = tempfile.mkstemp(prefix="state-", suffix=".tmp", dir=path.parent)
    temporary = Path(filename)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(state, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("show")
    commit = commands.add_parser("commit")
    commit.add_argument("--expected", type=int, required=True)
    commit.add_argument("--file", type=Path, required=True)
    args = parser.parse_args()
    workspace = Path(args.workspace).resolve(strict=True)
    if not workspace.is_dir():
        raise ValueError("workspace must be a directory")
    key = hashlib.sha256(os.path.normcase(str(workspace)).encode("utf-8")).hexdigest()[:24]
    codex_root = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    directory = codex_root / "figma-task-steward" / key
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / "state.json"
    with process_lock(directory / "transaction.lock"):
        state = read_state(path)
        if args.command == "commit":
            candidate = json.loads(args.file.read_text(encoding="utf-8-sig"))
            validate(candidate)
            if state["revision"] != args.expected or candidate["revision"] != args.expected:
                print(json.dumps({"error": "revision_conflict", "actual": state["revision"]}))
                return 2
            candidate["revision"] += 1
            atomic_write(path, candidate)
            state = candidate
    print(json.dumps({"path": str(path), "state": state}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, TypeError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
