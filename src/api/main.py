from __future__ import annotations

from fastapi import FastAPI

from src.common.schemas import DiagnosisRequest
from src.diagnosis.result_mapper import attach_result_text
from src.diagnosis.scoring import score_record


app = FastAPI(
    title="BAT Rule-based Diagnosis API",
    description="학습유형 질문지 기반 규칙 채점 API",
    version="1.0.0",
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/diagnose")
def diagnose(payload: DiagnosisRequest) -> dict:
    record = payload.model_dump()
    scored = score_record(record)
    enriched = attach_result_text(scored)
    return enriched
