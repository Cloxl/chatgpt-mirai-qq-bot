from typing import Any, Dict, List, Literal

from pydantic import BaseModel

from framework.workflow.core.dispatch import CombinedDispatchRule


class SimpleRule(BaseModel):
    """简单调度规则（单一条件）"""

    type: str
    config: Dict[str, Any] = {}  # 规则类型特定的配置


class RuleGroup(BaseModel):
    """规则组"""

    operator: Literal["and", "or"] = "or"
    rules: List[SimpleRule]


class DispatchRuleList(BaseModel):
    """调度规则列表"""

    rules: List[CombinedDispatchRule]


class DispatchRuleResponse(BaseModel):
    """调度规则响应"""

    rule: CombinedDispatchRule
