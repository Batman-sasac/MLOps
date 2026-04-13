from __future__ import annotations

from typing import Any, Dict
import math
import pandas as pd

from src.common.question_rules import QUESTION_RULES


KOREAN_TO_TRAIT = {
    "장독립형": "field_independent",
    "장의존형": "field_dependent",
    "숙고형": "reflective",
    "충동형": "impulsive",
}


def _is_missing(value: Any) -> bool:
    try:
        return value is None or (isinstance(value, float) and math.isnan(value)) or pd.isna(value)
    except Exception:
        return value is None


def _positive_trait(rule: Dict[str, str]) -> str:
    return "field_independent" if rule["axis"] == "axis1" else "reflective"


def _negative_trait(rule: Dict[str, str]) -> str:
    return "field_dependent" if rule["axis"] == "axis1" else "impulsive"


def normalize_single_answer(question_key: str, value: Any) -> str:
    if question_key not in QUESTION_RULES:
        raise KeyError(f"{question_key} 는 정의되지 않은 문항입니다.")

    if _is_missing(value):
        raise ValueError(f"{question_key} 응답이 비어 있습니다.")

    rule = QUESTION_RULES[question_key]

    if isinstance(value, str):
        normalized = value.strip()
        upper = normalized.upper()

        if upper in {"A", "B"}:
            return rule[f"{upper}_trait"]

        if normalized in KOREAN_TO_TRAIT:
            return KOREAN_TO_TRAIT[normalized]

        if normalized in {"1", "1.0"}:
            return _positive_trait(rule)
        if normalized in {"0", "0.0"}:
            return _negative_trait(rule)

    if isinstance(value, (int, float)) and not _is_missing(value):
        if float(value) == 1.0:
            return _positive_trait(rule)
        if float(value) == 0.0:
            return _negative_trait(rule)

    raise ValueError(
        f"{question_key} 값 '{value}' 를 해석할 수 없습니다. A/B, 0/1, 장독립형/장의존형/숙고형/충동형 중 하나를 사용하세요."
    )


def normalize_record(record: Dict[str, Any]) -> Dict[str, Any]:
    normalized = dict(record)
    for i in range(1, 21):
        q = f"q{i}"
        normalized[f"{q}_trait"] = normalize_single_answer(q, record.get(q))
    return normalized
