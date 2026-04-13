from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
from typing import List

import pandas as pd

from src.common.paths import PROCESSED_DIR
from src.diagnosis.result_mapper import attach_result_text
from src.diagnosis.scoring import score_record


def run_batch(csv_path: str) -> Path:
    df = pd.read_csv(csv_path)

    required_cols = [f"q{i}" for i in range(1, 21)]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"입력 CSV에 필수 문항 컬럼이 없습니다: {missing}")

    results: List[dict] = []
    for _, row in df.iterrows():
        record = row.to_dict()
        scored = score_record(record)
        enriched = attach_result_text(scored)
        results.append(enriched)

    result_df = pd.DataFrame(results)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    output_path = PROCESSED_DIR / f"diagnosis_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    result_df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"[완료] 결과 저장: {output_path}")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="규칙 기반 학습유형 진단 배치 실행")
    parser.add_argument("--survey-csv-path", required=True, help="입력 설문 CSV 경로")
    args = parser.parse_args()
    run_batch(args.survey_csv_path)


if __name__ == "__main__":
    main()
