from __future__ import annotations

from typing import Any, Dict

from src.common.result_texts import COMMON_FOOTER, TYPE_RESULT_TEXTS


def _resolve_type_key(axis1_trait: str, axis2_trait: str) -> str:
    for key, value in TYPE_RESULT_TEXTS.items():
        if value["axis1_trait"] == axis1_trait and value["axis2_trait"] == axis2_trait:
            return key
    raise KeyError(f"유형 조합을 찾을 수 없습니다: {axis1_trait}, {axis2_trait}")


def attach_result_text(scored_record: Dict[str, Any]) -> Dict[str, Any]:
    type_key = _resolve_type_key(scored_record["axis1_trait"], scored_record["axis2_trait"])
    text_info = TYPE_RESULT_TEXTS[type_key]

    result = dict(scored_record)
    result.update(
        {
            "final_type_key": text_info["final_type_key"],
            "final_type_kor": text_info["final_type_kor"],
            "summary_title": text_info["summary_title"],
            "traits_text": " | ".join(text_info["traits"]),
            "study_tips_text": " | ".join(text_info["study_tips"]),
            "relationship_tips_text": " | ".join(text_info["relationship_tips"]),
            "common_footer_text": " ".join(COMMON_FOOTER),
            "result_payload": {
                "final_type_key": text_info["final_type_key"],
                "final_type_kor": text_info["final_type_kor"],
                "summary_title": text_info["summary_title"],
                "traits": text_info["traits"],
                "study_tips": text_info["study_tips"],
                "relationship_tips": text_info["relationship_tips"],
                "common_footer": COMMON_FOOTER,
            },
        }
    )
    return result
