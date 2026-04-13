from __future__ import annotations

from typing import Any, Dict

from src.common.question_rules import TRAIT_KOR
from src.diagnosis.normalize import normalize_record


def _dominant(positive_score: int, negative_score: int, positive_trait: str, negative_trait: str) -> tuple[str, bool]:
    if positive_score == negative_score:
        return positive_trait, True
    return (positive_trait, False) if positive_score > negative_score else (negative_trait, False)


def score_record(record: Dict[str, Any]) -> Dict[str, Any]:
    normalized = normalize_record(record)

    scores = {
        "field_independent": 0,
        "field_dependent": 0,
        "reflective": 0,
        "impulsive": 0,
    }

    for i in range(1, 21):
        trait = normalized[f"q{i}_trait"]
        scores[trait] += 1

    axis1_trait, is_tie_axis1 = _dominant(
        scores["field_independent"], scores["field_dependent"], "field_independent", "field_dependent"
    )
    axis2_trait, is_tie_axis2 = _dominant(
        scores["reflective"], scores["impulsive"], "reflective", "impulsive"
    )

    result = dict(normalized)
    result.update(
        {
            "score_field_independent": scores["field_independent"],
            "score_field_dependent": scores["field_dependent"],
            "score_reflective": scores["reflective"],
            "score_impulsive": scores["impulsive"],
            "axis1_trait": axis1_trait,
            "axis2_trait": axis2_trait,
            "axis1_label": TRAIT_KOR[axis1_trait],
            "axis2_label": TRAIT_KOR[axis2_trait],
            "score_gap_axis1": abs(scores["field_independent"] - scores["field_dependent"]),
            "score_gap_axis2": abs(scores["reflective"] - scores["impulsive"]),
            "is_tie_axis1": is_tie_axis1,
            "is_tie_axis2": is_tie_axis2,
        }
    )
    return result
