---
name: unreal-project
description: Unreal Engine 项目通用约束。修改或分析 UE 代码、资产、Gameplay、音频、UMG 或架构时使用；涉及 Unreal 资产或可能回写资产工作区的 Git 操作时额外启用资产安全门禁。普通文档和只读 Git 查询不使用。
---

# Unreal 项目规范

所有项目路径相对于当前工作项目根目录，不相对于全局 Skill 安装目录。文档固定采用 [project-documentation](../project-documentation/SKILL.md) 的架构；项目专用引擎版本、工具和验证命令写入根目录 `AGENTS.md`，不搜索其他文档位置。

## 优先级与工作方式

- 以用户本次目标、明确范围和仓库现状为准。明确的小范围调参、换资源和已批准方案直接执行，不重复索要确认；新功能与玩法行为变更遵循 `AGENTS.md` 的方案流程。
- 只加载当前任务需要的代码和现存文档；文档维护遵循 `AGENTS.md`。
- 跨任务协调遵循项目 `AGENTS.md` 的消息边界：修改前只读核对实际写入或 Editor 操作冲突，确需协调时才联系相关任务，保持工作区和 Editor 单写者；不得仅因任务显示“活跃”就发送消息。
- 优先复用现有结构并完成可验证结果。不要主动增加占位功能、便利接口、调试可视化、自动回退、兼容层、未来扩展或无需求测试。
- 仅当缺少的决定会实质改变功能范围、公共契约、长期职责或不可恢复资产结果时暂停询问；先完成不依赖该决定的工作。
- 用户纠正范围后立即停止旧方向，保留已完成且仍符合新范围的工作。

## 现有行为复用

- 修改前检查同类功能的入口、流程、表现、资源和清理，简述参照、复用方式及差异；未找到时说明已查范围。
- 从公共入口复用完整行为，包括交互、动画、音效、聚焦、拾取、射后收尾及完成、中断、死亡、离场清理。公共实现统一负责参与者、启动与结束，不由事件各自拼装或补调收尾。
- 无法直接复用时只做必要提取，不另造同功能实现；保持已有参数、资源、时序与效果，差异按 `AGENTS.md` 确认，验收同时核对原功能与新功能。

## 架构与职责

改动会新增状态、跨模块流程、表现所有者、公共入口或移动现有职责时，在编码前简要确认这条关系：

```text
功能公共入口 → 状态所有者 → 规则/流程执行者 → 表现所有者
```

按 `AGENTS.md` 需要方案的任务，将这条关系与现有参照、具体文件／资产、行为差异和验证方式一起简要说明，不让美术代替 Codex 猜测技术归属。改变公共职责或网络权威归属时由项目负责人确认，已有批准不重复询问。

在 `AGENTS.md` 允许直接执行或方案已批准的范围内，局部修改明显属于现有职责时直接实施，无需为了输出关系链而停工。新增类或职责拆分如果是完成已批准目标的自然实现步骤，可以继续；只有存在多个会改变产品或公共架构的合理方案时才让用户选择。

- 状态、规则/流程、表现分离。权威状态类不拥有本地视觉或音频表现；表现类不决定规则结果。
- 对外保留窄门面。门面负责校验与转发，不吞入各子功能的具体实现和生命周期状态。
- 非简单逻辑具有独立职责、状态或生命周期，或移除后其他功能仍成立时，放入所属功能目录的独立单元。
- 按功能组织目录并优先复用现有目录；使用合适的 Unreal `Subsystem`、`Component`、`UObject` Controller、Executor 或 Presentation Actor，不机械套用 MVC。
- 不为追求小 diff 把新功能塞进已承担其他职责的大类；也不为形式上的分层拆出无独立职责的包装层。

## C++ 与 Blueprint 边界

- 行为逻辑默认使用 C++。Blueprint 保留模型、材质、动画、音频、Transform 和必要设计参数；只有引擎工作流确实要求时才在 Blueprint Graph 中写逻辑。
- 模型、材质、组件相对 Transform、可见性默认值等静态表现配置直接保存在生产 Blueprint 默认值中。C++ 构造函数、`OnConstruction` 和初始化流程不得通过硬编码资源路径、`SetStaticMesh`、`SetMaterial` 或 `SetRelativeTransform` 重复配置或覆盖它们。
- C++ 只有在运行时状态确实要求动态变化时才修改 Blueprint 配置的表现组件，并且只修改该行为所需的字段；不得借运行时初始化顺便校正导入轴向、尺寸、枢轴或美术默认值。模型自身需要统一轴向、尺寸或枢轴时，修改并烘焙源模型或 Static Mesh 资产。
- 编辑器或 Blueprint 暴露必须有设计用途。实例引用使用 `EditInstanceOnly`；默认配置放入 `<项目名>|Setup` 等项目 Category，具体命名遵循根目录 `README.md`。
- 仅供 C++ 内部播放、缓存或生命周期控制的组件和属性不使用 `BlueprintReadOnly`、`BlueprintReadWrite`、`Edit*` 或 `Visible*`；派生 Blueprint 无需调整组件本体时设置 `bEditableWhenInherited = false`。
- 设计师需要替换的资源和参数通过窄范围 `EditDefaultsOnly` 属性提供。
- 可调组件不设为根组件，支持在蓝图中统一调整并由关卡实例继承，避免逐实例覆盖 Transform。
- 场景 Actor 型 Manager 保留独立 Scene Root，并带无碰撞、游戏中隐藏的编辑器识别 Mesh 子组件；ActorComponent、Subsystem 等非场景管理器不适用。
- 运行时资源使用蓝图或 DataAsset 中序列化的类型化引用，禁止通过硬编码或拼接路径调用 `LoadObject`、`LoadClass`、`ConstructorHelpers` 或构造软路径。全局资源表使用当前项目明确配置的 DataAsset，并通过 Asset Manager 烘焙；具体资源名与内容目录记在根目录 `README.md`，不得假定已有固定名称的资源。配置文件中的资源选择及离线迁移、测试夹具路径不在此限。交付前执行根目录 `AGENTS.md` 中实际配置的资源引用检查命令；没有对应检查工具时核对本次引用并报告自动检查缺口，不调用不存在的脚本。

## Unreal Editor 与资产

- `.uasset`、`.umap` 或 Unreal Editor 实例的读取、修改、编译、保存和验证只使用已配置的 Unreal MCP；不使用鼠标、`computer-use`、无头 Commandlet 或直接改写二进制资产替代。
- Unreal MCP 缺少当前操作能力时，完成仍可进行的文本工作，并准确报告剩余的 Editor 验证或操作。
- C++、配置和文档等文本文件使用常规代码工具。
- 自动化关闭编辑器通过 Unreal MCP 执行根目录 `AGENTS.md` 明确配置、且已验证可用的正常关闭命令，或操作主窗口的 File → Exit；先保存，允许用户取消，确认所有项目 Editor 进程退出后才执行要求关闭编辑器的编译。不得假定新项目自带自定义关闭命令。UE 5.8 环境曾出现 `unreal.SystemLibrary.quit_editor()`、`QUIT_EDITOR` 和底层 RequestExit 跳过主窗口关闭通知、导致资产窗口晚于 Editor Subsystem 销毁而崩溃的问题；适用该问题的环境禁止使用这些入口。命令不可用时使用 File → Exit，不以强制退出替代正常关闭。
- Blueprint 创建、复制、编译及生成类/CDO 修改不放入 `ProgrammaticToolset.execute_tool_script` 的整批自动撤销事务。通过 MCP 分步调用或 MCP 的 Editor Python 入口，先核对对象路径、类型及属性，再创建、配置、编译、验证和保存；复制成功不代表后续步骤成功。`refPath` 使用工具返回的完整对象路径；设计默认值写到生成类的 CDO，不把 Blueprint 对象当成 CDO。
- 出现 `SkeletonCompiledBlueprints`、`ClassGeneratedBy is null` 或 Blueprint 编译期间的内部对象异常后，停止对该内存对象编译、撤销和重试。保存可确认的其他工作后正常重开，核对磁盘资产状态再恢复。不得用捕获异常后返回成功掩盖失败，也不依赖撤销恢复生成类。
- PIE 自动测试使用 UE 5.8、且引擎 `FStartPIEForAutomationCommand` 析构实现负责解除 root 时，给临时 `ULevelEditorPlaySettings` 显式 `AddToRoot()`；由该引擎命令析构执行 `RemoveFromRoot()`，包括测试取消路径；其他版本先核对同一生命周期约定，不照搬版本相关处理。不要仅依赖后续 latent command 持有设置对象，也不要在启动命令结束前自行解除 root。
- 资产修改或可能回写资产工作区的 Git 操作按需读取[资产与 Git 安全门禁](references/asset-safety.md)；恢复与备份统一遵循当前项目根目录 `README.md` 的“资产版本与临时备份”章节。

## UI 架构

```text
Designer WBP → 功能 UObject Controller → 所属 Subsystem / Gameplay API
```

- WBP 负责布局、样式、动画、导航和状态显示，默认继承 `UUserWidget`；正式 UI 不用原生 `RebuildWidget()` 或 Slate 重建 Widget Tree。
- Controller 负责控件契约、绑定与解绑、意图转发、ViewState 转换和视图更新；同一操作只绑定一次。
- Gameplay 模块负责网络、Travel、规则、服务器校验和权威状态；UI 不直接修改 `GameState`、`PlayerState` 等权威状态。
- 本地 `PlayerController` 或 `HUD` 只组装 WBP、Controller 与依赖，并负责清理。
- Controller 头文件和源文件按需保持同序：初始化与清理、视图绑定、功能操作、事件处理、视图状态转换。注释只解释意图。

## Blueprint 表现资产

- 可由设计或美术替换模型、材质、相对位置、缩放、动画或局部反馈的世界表现物，生产实例使用 Blueprint；C++ 提供行为基类和窄表现契约，不硬编码最终造型或可调 Transform。
- 可独立替换的实体道具使用所属功能目录下的 Blueprint；统一表现 Actor 通过 Blueprint 类引用或 Child Actor 组装。
- 默认运行类指向正式 Blueprint 资产。资源在 Blueprint 默认值中配置，C++ 负责状态投影、生命周期和交互桥接。
- Blueprint 不拥有服务器权威状态、私密答案、合法性校验、随机结果、复制边界或结算。
- 纯内部且无设计调节需求的实现组件无需额外包装成 Blueprint。

## 内容与文档

- 内容路径和命名遵循当前项目根目录 `README.md` 中约定的内容根目录，并核对实际资源结构；不假定项目名或固定的 Content 子目录。
- 稳定职责写入对应模块指南的架构章节，不维护独立的全项目架构文档，也不记录临时工具、测试实现、兼容代码或计划删除内容。
- 模块维护地图中，同名 `.h/.cpp` 合并为一个不带后缀的类名条目，每个类一句话说明整体职责；只有单个文件时保留实际文件名。
- 只有用户明确要求或仓库规则要求同步时才启动 `$project-documentation`。

## 验证与交付

- 运行与改动风险匹配的最小有效验证。通过后不重复扩大测试，除非出现新失败或未解决风险。
- 修复缺陷时先稳定复现并记录失败信号；修复后先重跑该最小复现，再跑覆盖实际用户链路的目标测试。已知失败、崩溃或卡死没有解释并处理前，不宣称完成。
- 区分产品缺陷和测试夹具缺陷：以运行时事实、正式 Ruleset/资产配置和端到端结果为准，不用过期硬编码断言改写生产行为。
- UI 改动验证真实操作链路；联网改动验证主机和客户端；输入改动验证鼠标、焦点与游戏输入恢复。
- 不能运行 Editor 验证时，清楚区分已验证内容与仍需人工确认的事项。
- 最终报告实际修改、验证结果和剩余事项。
