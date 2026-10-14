[English](README.md) | 简体中文

# Senler Skills

以当前本地版本为准的六个 Skill，保留需求澄清、方案、实施、审查和文档维护规则。
新功能和行为变更先用 `grilling`，再由 `ask-plan-build` 承接已有答案出方案，确认后实施。
明确的小范围修改和已批准方案直接执行，不重复提问或审批。

| Skill | 用途 |
| --- | --- |
| `setup-senler-skills` | 按固定文档架构一次初始化项目，使用当前本地 Skill。 |
| `grilling` | 按决策依赖澄清需求，整理效果、边界和验收；已有答案不重问。 |
| `ask-plan-build` | 承接澄清结论，说明具体改动与验证，确认后实施并收尾。 |
| `unreal-project` | UE 的职责边界、C++ 与蓝图分工、UI、资产操作及验证规则。 |
| `code-review` | 检查本次完整改动的规范、需求、文档与验证；只审查，不自动提交。 |
| `project-documentation` | 按固定文档架构维护已确认事实，一项事实只维护一处。 |

## 一条命令安装全部

安装 Node.js（22.20 或更新版本）和 Git 后，在终端运行：

```sh
npx --yes skills add senler007/skills --skill '*' --agent codex --global --copy --yes
```

这会将本仓库当前的六个完整 Skill 安装到本机 Codex 的全局技能位置，供各项目共用。
GitHub 是发布来源，Codex 实际读取本机安装文件；项目内不需要再放同名副本。
命令会更新同名全局 Skill，执行前请先保留自己尚未发布的本地修改。
曾安装过旧版的人需自行移除已不再使用的旧 Skill；该命令不会卸载其他已安装包。

## 新项目一键初始化

完成上面的全局安装后，在 Codex 打开新项目目录，发送：

```text
使用 $setup-senler-skills 初始化当前项目。
```

也可以一次附上项目名称、用途和核心体验，减少补充问答。初始化会读取当前工程事实，
直接生成 `AGENTS.md`、`README.md`、`CONTEXT.md`、`Docs/ProjectOverview.md`，
并写入 grilling → ask-plan-build → 确认后实施的流程。未知的项目事实只问必要缺项。
世界观和模块指南按下文的实际条件建立；已有文件保留内容、合并缺项，重复运行不重复插入规则。

初始化入口及其伴随技能使用当前本地版本，不从 GitHub 拉取旧版、不重装技能。
它只初始化文档与规则，不创建 UE 工程或连接 Figma。安装入口尚未出现在技能列表时，
重新打开项目会话；仍未刷新可重启 Codex。

## 固定文档架构

使用本套 Skill 必须采用下列路径和职责，不兼容其他文档布局，不自动寻找替代文件。
全部路径都相对于当前工作项目根目录，与 Skill 的全局安装位置无关。

| 项目文档 | 固定职责 |
| --- | --- |
| `AGENTS.md` | 团队规则、开发流程、Skill 入口、项目专用约束和实际工具命令 |
| `README.md` | 运行方式、资源目录、命名规范、资产版本与临时备份规则 |
| `CONTEXT.md` | 项目术语与含义 |
| `Docs/ProjectOverview.md` | 项目简介、核心体验、文档导航和参考资料链接（如 Figma） |
| `Docs/Worldbuilding.md` | 世界观与角色设定，仍为可选文档 |
| `Docs/Modules/<功能名>.md` | 模块行为、设计、职责、实现与维护入口、稳定验证方式 |

前四份为必需项目文档；模块指南随实际模块建立，世界观文档按需使用。
接入时按指定路径补齐已确认内容；未知事实需补充，不编造、不创建空占位。
只读调查和审查只报告缺失，不顺带创建文件。
不生成每日开发记录，不建立独立架构文档，不恢复已删除的旧配置。
具体维护规则以 [project-documentation](skills/project-documentation/SKILL.md) 为准。

## 安装与使用

将 `skills/` 下的六个完整文件夹安装到 Agent 的技能目录，可以全局共用。
保留包内的 `references/`、`agents/` 等已有附带文件。项目文档仍放在各自项目根目录。
不要把本仓库根目录的 `AGENTS.md` 当作业务项目的工作规则直接复制。

例如：

- `用 $grilling 澄清这个新功能，结论交给 ask-plan-build 形成方案。`
- `用 $ask-plan-build 承接已经确认的需求，给出具体方案。`
- `用 $code-review 检查本次尚未提交的改动。`
- `用 $project-documentation 按规定的文档架构更新已确认的功能说明。`

Unreal 任务另外使用 `unreal-project`；非 UE 任务不会套用 UE 专用规则。
项目内容根目录、资源表名称写入项目 `README.md`；引擎版本、实际关闭编辑器命令和验证命令
写入项目 `AGENTS.md`。不假定每个项目都存在同名资产、脚本或自定义工具。
版本相关故障处理保留在 Skill 中，按标明的版本和条件应用。

修改流程默认不自动提交或推送。发布、跨会话消息和任务协调另按用户实际授权进行。

## 来源

借鉴 Matt Pocock 的 AIHero Skills，由 senler007 独立维护，使用 [MIT 许可](LICENSE)。
