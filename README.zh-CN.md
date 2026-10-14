[English](README.md) | 简体中文

# Senler Skills

把项目初始化、需求澄清、方案实施、UE 规范、审查、文档维护和 Figma 任务管家
放在同一套工作流里。**一条命令把全部 12 个 Skill 装到全局，新项目再用一句话初始化。**
通用规则全局复用，项目自己的资料留在项目里。

## 一次安装全部

安装 Node.js/npm 和 Git 后，在终端执行：

```bash
npx --yes skills add senler007/skills --skill '*' --agent codex --global --copy --yes
```

命令通过 [Skills CLI](https://github.com/vercel-labs/skills) 安装本仓库全部 Skill，
包含引用文档和辅助脚本。`--global` 表示全局，`--copy` 使用复制方式，无需创建符号链接。
安装会更新同名全局版本，有个人改动时先保留自己的版本。看不到新 Skill 时重启 Codex。
安装本身不修改当前项目，也不连接外部账户。

## 新项目怎么用

在 Codex 打开新项目目录，发送：

```text
使用 $setup-senler-skills 初始化当前项目，使用已经安装的全局 Skill。
检查并复用已有资料，建立或合并项目文档、文档导航和开发流程。
```

AI 会检查当前项目，只问缺失的必要信息，再生成或合并文档。已有项目也用同一句话；
保留原文档与约定，不重复建一套，不把 Skill 再复制进每个项目。
如果项目里已有同名 Skill，会核对差异并明确采用哪个来源。

文档按下列职责组织，已有项目沿用自己的路径；有实际内容才建文件：

| 文档 | 内容 |
| --- | --- |
| `AGENTS.md` | 项目规则、开发流程、Skill 和文档入口 |
| `README.md` | 如何运行项目、仓库与资源目录、命名规范 |
| `Docs/ProjectOverview.md` | 项目简介、核心体验、文档导航、Figma 等参考资料 |
| `CONTEXT.md` | 项目术语与含义 |
| `Docs/Worldbuilding.md` | 有世界观需求时维护已确定的设定 |
| `Docs/Modules/<功能名>.md` | 已有模块的行为、职责、实现与维护入口 |

不用为了凑齐目录建空文档；不默认创建开发日志或独立架构文档。

## 日常开发

新功能或行为变更采用：

```text
查项目事实 → grilling 澄清 → ask-plan-build 出方案 → 用户确认
          → 实施与验证 → code-review → 同步已变化的项目文档
```

`grilling` 的结论直接交给 `ask-plan-build`，不重新问一轮相同问题。
需求已经明确时，整理一下结论即可。明确的小改动、已批准方案直接执行。
UE 任务同时遵循 `unreal-project`。

例如：

```text
使用 $grilling，给这个项目增加保存和切换角色外观方案的功能。
```

之后按问题补充需求、确认具体方案，AI 再实施、验证和收尾。只讨论设计时不会自动开始实现。

## 全部 Skill

| Skill | 用途 |
| --- | --- |
| `setup-senler-skills` | 为新旧项目初始化文档与流程 |
| `grilling` | 按决策依赖澄清需求 |
| `ask-plan-build` | 承接结论，给出方案，批准后实施 |
| `unreal-project` | UE 的 C++、蓝图、界面、资产与验证规范 |
| `code-review` | 检查规范、需求和文档，覆盖尚未提交的修改 |
| `project-documentation` | 维护已确认的项目事实和模块指南 |
| `figma-task-steward` | 管理 Figma 任务、独立会话、串行写入与交接 |
| `grill-with-docs` | 澄清后将最终确认的设计写入文档 |
| `to-spec` | 为单次变更形成简明规格 |
| `to-tickets` | 把规格拆成可交付的任务 |
| `implement` | 执行明确选择的 Spec/Ticket 工作流 |
| `tdd` | 围绕可观察行为进行测试驱动开发 |

全部一起安装，使用时根据任务调用。原有 Spec/Ticket 流程仍可显式选择，
只运行这次变更真正需要的阶段，也可以把 Spec 或一组 Tickets 直接交给 `implement`。
默认功能流程不强制建 Issue、拆 Ticket 或提交 Git。

## Figma 与 UE 的首次连接

Figma 管家需要已连接的 Figma 插件、Codex 桌面端的项目与会话工具，以及 Python 3.8+。
初始化时提供自己项目的 Figma 文件与任务页，明确启用任务协调和需要的写回范围。
每日自动接班的时间由使用者指定；安装不会自动创建定时任务。

UE 资产操作需要当前项目可用的编辑器集成。缺少连接时会指出具体缺项，
不影响其他文档和流程的初始化。包里不包含作者的项目链接、账本、私人路径或授权。

完整操作说明见 [安装与使用](docs/INSTALL.zh-CN.md)。更新整套 Skill 时重新执行安装命令；
它只更新全局包，项目里的规则需要调整时再运行初始化，不覆盖项目自己的资料。

## 来源

参考 Matt Pocock 的 AIHero Skills 工作流，由 senler007 独立维护，采用 MIT 许可证。
保留原作者归属，不自动同步上游。见 [LICENSE](LICENSE)。
