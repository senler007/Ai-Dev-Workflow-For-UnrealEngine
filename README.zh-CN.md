[English](README.md) | 简体中文

# Senler Skills

这是我在游戏开发中整理的一套精简的AI协作流程，也准备继续用在后面的项目里。
主要解决 : 
1. 文档位置与职责划分清楚
2. 制作流程统一并且减少错误

项目越做越大，文档和需求制作如果不明确，AI就容易到处拉屎。这套 Skill 把文档放哪里、需求怎么问、方案怎么做、完成后怎么检查统一起来,包含了一套简单的UE项目制作管线。

## 安装与初始化
先用指令 : 
```sh
npx --yes skills add senler007/Ai-Dev-Workflow --skill '*' --agent codex --global --copy --yes
```
然后在 Codex 打开新项目，发送下面这句话

```text
使用 $setup-senler-skills 初始化当前项目。
```


## 做游戏必需的项目文档
项目一定要有明确的文档风格,不然后面会很痛苦.
使用我这套 Skill，就统一采用下面的通用文档架构。路径都相对于自己的项目根目录。
- Docs/ProjectOverview.md : 项目简介、核心体验、文档导航与其他重要资料(如figma参考等)的放置处
- AGENTS.md : 团队工作规则、开发流程与 Skill 入口
- README.md : 仓库说明、资源目录、命名与资产管理规范
- CONTEXT.md : 项目术语及其含义
- Docs/Worldbuilding.md : 世界观(可选,一般放一些文学类的东西)
- Docs/Modules/<功能名>.md ：实际模块的设计、职责、实现与维护入口，随功能需要建立。

## 需求制作流程

**不管什么需求,只需要用到一个skill,就是在提出需求的时候用$grilling.他会一直问你需求里的不清晰之处.做任何功能都可以用这个,防止返工或不满意** , 其他skill都是自动调用的不需要自己调用.想了解可以了解一下

| Skill | 做什么 |
| --- | --- |
| `setup-senler-skills` | 初始化项目文档和开发流程。 |
| `grilling` | 澄清需求、边界和验收标准。 |
| `ask-plan-build` | 承接澄清结论，出方案，确认后实施。 |
| `unreal-project` | 约束 UE 项目的 C++ 与蓝图分工、资源组织、资产操作和验证。 |
| `code-review` | 检查改动是否符合需求与项目规则。 |
| `project-documentation` | 维护项目文档，保持内容和实现一致。 |
| `figma-task-steward` | 管理 Figma 任务，分配独立会话，串行实施并交接，减少反复协调。 |

**最后祝你牛逼Bro**