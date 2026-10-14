[English](README.md) | 简体中文

# Senler Skills

这是我在游戏开发中整理的一套 AI 协作流程，也准备继续用在后面的项目里。
项目越做越大，需求和文档如果没有明确分工，AI 就容易重复提问、到处写文档，最后还得返工。这套 Skill 把文档放哪里、需求怎么问、方案怎么做、完成后怎么检查统一起来。

## 安装与初始化

准备好 Node.js 22.20+ 和 Git，一条命令安装全部七个 Skill：

```sh
npx --yes skills add senler007/skills --skill '*' --agent codex --global --copy --yes
```

全局安装一次，各项目共用，不需要在项目里再放副本。更新会覆盖同名 Skill，自己改过的内容先保留。

在 Codex 打开新项目，发送下面这句话，附上项目名称、用途和核心体验即可：

```text
使用 $setup-senler-skills 初始化当前项目。
```

它会建立项目文档和开发规则，已有内容保留并补齐。加入已经接入这套流程的项目，只需安装 Skill、同步项目最新版，再开一个 Codex 会话，不必重新初始化。

## 项目文档

使用这套 Skill，就统一采用下面的文档架构。路径都相对于自己的项目根目录。

- `Docs/ProjectOverview.md`：项目简介、核心体验、文档导航，以及 Figma 等参考资料入口。
- `AGENTS.md`：团队工作规则、开发流程、Skill 入口和项目专用命令。
- `README.md`：项目运行方式、资源目录、命名与资产管理规范。
- `CONTEXT.md`：项目术语及其含义。
- `Docs/Worldbuilding.md`：世界观与角色设定，按需使用。
- `Docs/Modules/<功能名>.md`：实际模块的设计、职责、实现与维护入口，随功能需要建立。

同一件事只在一处维护，不到处重复写。详细规则见 [project-documentation](skills/project-documentation/SKILL.md)。

## 需求怎么做

**做新功能时，先用 `$grilling` 把需求说清楚。** 它会追问真正不清楚的地方，减少做到一半再推翻的情况；需求已经明确就直接整理，不为了提问而提问。

接着由 `ask-plan-build` 承接结论，形成具体方案，确认后实施；完成后检查改动，并同步需要更新的文档。已经回答的问题不再问，明确的小修改和已批准方案直接执行。

| Skill | 做什么 |
| --- | --- |
| `setup-senler-skills` | 初始化项目文档和开发流程。 |
| `grilling` | 澄清需求、边界和验收标准。 |
| `ask-plan-build` | 承接澄清结论，出方案，确认后实施。 |
| `unreal-project` | 约束 UE 项目的 C++ 与蓝图分工、资源组织、资产操作和验证。 |
| `code-review` | 检查改动是否符合需求与项目规则。 |
| `project-documentation` | 维护项目文档，保持内容和实现一致。 |
| `figma-task-steward` | 管理 Figma 任务，分配独立会话，串行实施并交接，减少反复协调。 |

日常不用逐个点名，按项目规则和任务需要使用；UE 规则只用于 UE 项目。需要 Figma 管家时，先连接 Figma 工具、准备 Python 3，把文件入口写入 `Docs/ProjectOverview.md`，再说：

```text
使用 $figma-task-steward 管理本项目的 Figma「每日安排」，创建独立任务会话并协调执行。
```

安装不会自动启动管家或创建日程。项目的协调授权和换班安排放在 `AGENTS.md`。

---

借鉴 Matt Pocock 的 AIHero Skills，由 senler007 独立维护，使用 [MIT 许可](LICENSE)。
