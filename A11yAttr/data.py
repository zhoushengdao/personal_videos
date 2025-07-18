"""WAI-ARIA 1.2 属性介绍"""

NL = "\n\t\t●"
NLP = "\n\t\t\t"

# https://www.w3.org/TR/wai-aria/#state_prop_def
ARIA_ATTRIBUTES_DATA = [
    {
        "name": "aria-activedescendant",
        "description": "当 DOM 焦点位于复合组件、组合框、文本框、分组或应用程序时，标识\n当前活动元素。",
        "value": f"取值：ID 引用{NL}即指向同一文档中另一个元素的 ID 引用",
    },
    {
        "name": "aria-atomic",
        "description": "指示辅助技术将根据 aria-relevant 属性定义的变更通知，完整呈现变更\n区域还是部分呈现。",
        "value": "取值：true/false"
        f"{NL}false（默认）：辅助技术仅呈现变更的节点"
        f"{NL}true：辅助技术将整个变更区域作为整体呈现，包含作者定义的标{NLP}签（若存在）",
    },
    {
        "name": "aria-autocomplete",
        "description": "指示输入文本是否会触发显示组合框、搜索框或文本框的用户预期值预测，\n并指定预测的呈现方式。",
        "value": "取值：inline/list/both/none"
        f"{NL}inline：用户输入时，可以动态插入建议的文本至光标后方"
        f"{NL}list：用户输入时，可以显示一个包含候选值集合的元素"
        f"{NL}both：用户输入时，可以显示一个包含候选值集合的元素。若显示，{NLP}则会自动选中其中一个值，且完成该选中值所需的补全文本将出现{NLP}在输入光标之后"
        f"{NL}none（默认）：用户输入时不显示自动预测建议",
    },
    {
        "name": "aria-busy",
        "description": "指示元素正在被修改，辅助技术可以等待修改完成后再向用户呈现这些变更。",
        "value": f"取值：true/false{NL}false（默认）：元素无预期更新{NL}true：元素正在更新",
    },
    {
        "name": "aria-checked",
        "description": "指示复选框、单选按钮等组件的当前“选中”状态。参见 aria-pressed 和\naria-selected。",
        "value": "取值：true/false/mixed/undefined"
        f"{NL}false：元素支持选中但当前未选中"
        f"{NL}mixed：三态复选框或菜单项复选框的混合模式值"
        f"{NL}true：元素已选中"
        f"{NL}undefined（默认）：元素不支持选中",
    },
    {
        "name": "aria-colcount",
        "description": "定义表格、网格或树形网格的总列数。参见 aria-colindex。",
        "value": f"取值：整数{NL}即不带小数部分的数值",
    },
    {
        "name": "aria-colindex",
        "description": "定义元素在表格、网格或树形网格中的列索引或位置。参见 aria-colcount\n和 aria-colspan。",
        "value": f"取值：整数{NL}即不带小数部分的数值",
    },
    {
        "name": "aria-colspan",
        "description": "定义单元格或网格单元在表格、网格或树形网格中跨越的列数。参见\naria-colindex 和 aria-rowspan。",
        "value": f"取值：整数{NL}即不带小数部分的数值",
    },
    {
        "name": "aria-controls",
        "description": "标识受当前元素控制内容或存在的元素。参见 aria-owns。",
        "value": f"取值：ID 引用列表{NL}即一个或多个 ID 引用的列表",
    },
    {
        "name": "aria-current",
        "description": "指示代表容器或相关元素集合中当前项的元素。",
        "value": "取值：page/step/location/date/time/true/false"
        f"{NL}page：表示页面集合中的当前页"
        f"{NL}step：表示流程中的当前步骤"
        f"{NL}location：表示环境或上下文中的当前位置"
        f"{NL}date：表示日期集合中的当前日期"
        f"{NL}time：表示时间集合中的当前时间"
        f"{NL}true：表示集合中的当前项"
        f"{NL}false（默认）：不代表集合中的当前项",
    },
    {
        "name": "aria-describedby",
        "description": "标识描述对象的元素。参见 aria-labelledby。",
        "value": f"取值：ID 引用列表{NL}即一个或多个 ID 引用的列表",
    },
    {
        "name": "aria-details",
        "description": "标识为对象提供详细扩展描述的元素。参见 aria-describedby。",
        "value": f"取值：ID 引用{NL}即指向同一文档中另一个元素的 ID 引用",
    },
    {
        "name": "aria-disabled",
        "description": "指示元素可感知但被禁用，因此不可编辑或操作。参见 aria-hidden 和\naria-readonly。",
        "value": f"取值：true/false{NL}false（默认）：元素启用{NL}true：元素及所有可聚焦后代均被禁用，且用户无法更改其值",
    },
    {
        "name": "aria-dropeffect",
        "description": "[在 ARIA 1.1 中弃用] 指示拖拽对象释放至放置目标时可执行的功能。",
        "value": "取值：以下限定值中的一个或多个组成的列表"
        f"{NL}copy：源对象副本将被放入目标"
        f"{NL}execute：使用拖拽源作为输入执行放置目标支持的功能"
        f"{NL}link：将在目标对象中创建拖拽对象的引用或快捷方式"
        f"{NL}move：源对象将从当前位置移除并放入目标"
        f"{NL}none（默认）：无法执行任何操作；尝试放置到此对象将取消拖{NLP}拽操作。与其他令牌值组合时忽略（如 'none copy' 等效于 'copy'）"
        f"{NL}popup：存在弹出菜单或对话框供用户选择拖拽操作（复制、移动、{NLP}链接、执行）及其他功能（如取消）",
    },
    {
        "name": "aria-errormessage",
        "description": "标识为对象提供错误消息的元素。参见 aria-invalid 和 aria-describedby。",
        "value": f"取值：ID 引用{NL}即指向同一文档中另一个元素的 ID 引用",
    },
    {
        "name": "aria-expanded",
        "description": "指示此元素拥有或控制的分组元素处于展开或折叠状态。",
        "value": "取值：true/false/undefined"
        f"{NL}false：此元素拥有或控制的分组元素已折叠"
        f"{NL}true：此元素拥有或控制的分组元素已展开"
        f"{NL}undefined（默认）：元素不拥有或控制可展开的分组元素",
    },
    {
        "name": "aria-flowto",
        "description": "标识下一个（或多个）元素在内容替代阅读顺序中的位置，允许辅助技术\n根据用户意图覆盖文档源码顺序的默认阅读方式。",
        "value": f"取值：ID 引用列表{NL}即一个或多个 ID 引用的列表",
    },
    {
        "name": "aria-grabbed",
        "description": "[在 ARIA 1.1 中弃用] 指示元素在拖拽操作中的“抓取”状态。",
        "value": "取值：true/false/undefined"
        f"{NL}false：元素支持被拖拽"
        f"{NL}true：元素已被“抓取”准备拖拽"
        f"{NL}undefined（默认）：元素不支持被拖拽",
    },
    {
        "name": "aria-haspopup",
        "description": "指示可通过元素触发的交互式弹出元素（如菜单或对话框）的可用性和类型。",
        "value": "取值：false/menu/listbox/tree/grid/dialog"
        f"{NL}false（默认）：元素无弹出框"
        f"{NL}true：弹出框为菜单"
        f"{NL}menu：弹出框为菜单"
        f"{NL}listbox：弹出框为列表框"
        f"{NL}tree：弹出框为树形结构"
        f"{NL}grid：弹出框为网格"
        f"{NL}dialog：弹出框为对话框",
    },
    {
        "name": "aria-hidden",
        "description": "指示元素是否暴露给无障碍 API。参见 aria-disabled。",
        "value": "取值：true/false/undefined"
        f"{NL}false：元素暴露给无障碍 API，如同已渲染"
        f"{NL}true：元素对无障碍 API 隐藏"
        f"{NL}undefined（默认）：元素隐藏状态由用户代理根据是否渲染决定",
    },
    {
        "name": "aria-invalid",
        "description": "指示输入值不符合应用程序的预期格式。参见 aria-errormessage。",
        "value": "取值：grammar/false/spelling/true"
        f"{NL}grammar：检测到语法错误"
        f"{NL}false（默认）：输入值没有检测到错误"
        f"{NL}spelling：检测到拼写错误"
        f"{NL}true：用户输入的值未通过验证",
    },
    {
        "name": "aria-keyshortcuts",
        "description": "指示作者为激活元素或赋予焦点实现的键盘快捷键。",
        "value": f"取值：字符串{NL}即无约束的值类型",
    },
    {
        "name": "aria-label",
        "description": "定义标记当前元素的字符串值。参见 aria-labelledby。",
        "value": f"取值：字符串{NL}即无约束的值类型",
    },
    {
        "name": "aria-labelledby",
        "description": "标识标记当前元素的元素。参见 aria-describedby。",
        "value": f"取值：ID 引用列表{NL}即一个或多个 ID 引用的列表",
    },
    {
        "name": "aria-level",
        "description": "定义元素在结构中的层级。",
        "value": f"取值：整数{NL}即不带小数部分的数值",
    },
    {
        "name": "aria-live",
        "description": "指示元素将被更新，并描述用户代理、辅助技术和用户可以预期的来自实\n时区域的更新类型。",
        "value": "取值：assertive/off/polite"
        f"{NL}assertive：区域更新具有最高优先级，应立即呈现给用户"
        f"{NL}off（默认）：除非用户当前聚焦该区域，否则更新不应呈现"
        f"{NL}polite：应在适当时机（如说完当前句子或用户暂停输入时）呈现{NLP}区域更新",
    },
    {
        "name": "aria-modal",
        "description": "指示元素显示时是否为模态框。",
        "value": "取值：true/false"
        f"{NL}false（默认）：元素不是模态框"
        f"{NL}true：元素是模态框",
    },
    {
        "name": "aria-multiline",
        "description": "指示文本框是否接受多行输入。",
        "value": "取值：true/false"
        f"{NL}false（默认）：单行文本框"
        f"{NL}true：多行文本框",
    },
    {
        "name": "aria-multiselectable",
        "description": "指示用户是否可从当前可选后代中选择多个项。",
        "value": "取值：true/false"
        f"{NL}false（默认）：仅能选择一项"
        f"{NL}true：组件中可同时选择多项",
    },
    {
        "name": "aria-orientation",
        "description": "指示元素方向为水平、垂直或未知/不明确。",
        "value": "取值：horizontal/undefined/vertical"
        f"{NL}horizontal：元素为水平方向"
        f"{NL}undefined（默认）：元素方向未知/不明确"
        f"{NL}vertical：元素为垂直方向",
    },
    {
        "name": "aria-owns",
        "description": "标识元素以定义 DOM 无法表示的父子关系（视觉、功能或上下文）。\n参见 aria-controls。",
        "value": f"取值：ID 引用列表{NL}即一个或多个 ID 引用的列表",
    },
    {
        "name": "aria-placeholder",
        "description": "定义控件无值时辅助用户输入数据的简短提示（单词或短语）。提示可为\n示例值或预期格式的简述。",
        "value": f"取值：字符串{NL}即无约束的值类型",
    },
    {
        "name": "aria-posinset",
        "description": "定义元素在当前列表项或树形项集合中的序号或位置。若集合中所有元素\n均存在于 DOM 则非必需。参见 aria-setsize。",
        "value": f"取值：整数{NL}即不带小数部分的数值",
    },
    {
        "name": "aria-pressed",
        "description": "指示切换按钮的当前“按下”状态。参见 aria-checked 和 aria-selected。",
        "value": "取值：true/false/mixed/undefined"
        f"{NL}false：元素支持按下但当前未按下"
        f"{NL}mixed：三态切换按钮的混合模式值"
        f"{NL}true：元素已按下"
        f"{NL}undefined（默认）：元素不支持按下",
    },
    {
        "name": "aria-readonly",
        "description": "指示元素不可编辑但可操作。参见 aria-disabled。",
        "value": "取值：true/false"
        f"{NL}false（默认）：用户可设置元素值"
        f"{NL}true：用户不可更改元素值",
    },
    {
        "name": "aria-relevant",
        "description": "指示实时区域内无障碍树变更时用户代理将触发的通知类型。参见\naria-atomic。",
        "value": "取值：以下限定值中的一个或多个组成的列表"
        f"{NL}additions：节点添加至实时区域的无障碍树"
        f'{NL}additions text（默认）：等效于 "additions text" 组合值'
        f'{NL}all：等效于 "additions removals text" 组合值'
        f"{NL}removals：实时区域内文本内容、文本替代项或节点从无障碍树移除"
        f"{NL}text：文本内容或文本替代项添加至实时区域无障碍树的任何后代",
    },
    {
        "name": "aria-required",
        "description": "指示表单提交前是否需要用户输入。",
        "value": "取值：true/false"
        f"{NL}false（默认）：表单提交时无需用户输入"
        f"{NL}true：表单提交前需在元素上提供输入",
    },
    {
        "name": "aria-roledescription",
        "description": "定义元素角色的人类可读、作者本地化描述。",
        "value": f"取值：字符串{NL}即无约束的值类型",
    },
    {
        "name": "aria-rowcount",
        "description": "定义表格、网格或树形网格的总行数。参见 aria-rowindex。",
        "value": f"取值：整数{NL}即不带小数部分的数值",
    },
    {
        "name": "aria-rowindex",
        "description": "定义元素在表格、网格或树形网格中的行索引或位置。参见 aria-rowcount\n和 aria-rowspan。",
        "value": f"取值：整数{NL}即不带小数部分的数值",
    },
    {
        "name": "aria-rowspan",
        "description": "定义单元格或网格单元在表格、网格或树形网格中跨越的行数。参见\naria-rowindex 和 aria-colspan。",
        "value": f"取值：整数{NL}即不带小数部分的数值",
    },
    {
        "name": "aria-selected",
        "description": "指示各类组件的当前“选中”状态。参见 aria-checked 和 aria-pressed。",
        "value": "取值：true/false/undefined"
        f"{NL}false：可选元素未选中"
        f"{NL}true：可选元素已选中"
        f"{NL}undefined（默认）：元素不可选",
    },
    {
        "name": "aria-setsize",
        "description": "定义当前列表项或树形项集合中的项数。若集合中所有元素均存在于 DOM\n则非必需。参见 aria-posinset。",
        "value": f"取值：整数{NL}即不带小数部分的数值",
    },
    {
        "name": "aria-sort",
        "description": "指示表格或网格中的项是否按升序或降序排序。",
        "value": "取值：ascending/descending/none/other"
        f"{NL}ascending：项目按该列升序排列"
        f"{NL}descending：项目按该列降序排列"
        f"{NL}none（默认）：该列未定义排序规则"
        f"{NL}other：已应用升序/降序外的排序算法",
    },
    {
        "name": "aria-valuemax",
        "description": "定义范围组件的最大值。",
        "value": f"取值：数值{NL}即任意实数",
    },
    {
        "name": "aria-valuemin",
        "description": "定义范围组件的最小值。",
        "value": f"取值：数值{NL}即任意实数",
    },
    {
        "name": "aria-valuenow",
        "description": "定义范围组件的当前值。参见 aria-valuetext。",
        "value": f"取值：数值{NL}即任意实数",
    },
    {
        "name": "aria-valuetext",
        "description": "定义范围组件 aria-valuenow 的人类可读文本替代。",
        "value": f"取值：字符串{NL}即无约束的值类型",
    },
]
