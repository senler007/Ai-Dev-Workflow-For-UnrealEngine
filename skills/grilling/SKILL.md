---
name: grilling
description: 新功能或行为变更的需求澄清入口；用户要求追问、挑战方案时也使用。明确的小范围修改和已批准方案的执行不重复澄清。
---

# 把需求问清楚

项目路径均相对于当前工作项目根目录；文档采用 [project-documentation](../project-documentation/SKILL.md) 规定的固定架构，不搜索或兼容其他文档布局。Skill 可以全局安装，不要求复制到项目内。

- 新功能或行为变更先在这里澄清需求，再交给 `ask-plan-build`；已有澄清结论直接沿用，只处理新增或变化的需求。
- 先读项目相关事实和已有答案，再按决策依赖提问。每轮只问当前能决定的一小组问题，并给建议及取舍。需求已清楚时简要整理结论并进入方案阶段，不为使用 Skill 凑问题。
- 问用户体验、范围和验收；游戏任务关注玩家体验。技术归属先查 `AGENTS.md`、对应 `Docs/Modules/` 指南和已有功能；Unreal 任务再使用 [unreal-project](../unreal-project/SKILL.md)。
- 后续问题依据回答调整；没有冲突证据，不重开已确定的选择。关键问题解决就结束，不穷举假设。
- 最后整理已确定效果、边界和待定项；需要实施时交给 [ask-plan-build](../ask-plan-build/SKILL.md)，复用这些答案直接形成方案，不再访谈一遍。
- 本 Skill 只澄清，不把讨论当作实施授权。仅在用户要求保存且确认整理结果后，用 [project-documentation](../project-documentation/SKILL.md) 更新已有文档，不保存问答流水账。
