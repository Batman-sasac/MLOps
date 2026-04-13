from typing import Optional
from pydantic import BaseModel, Field


class DiagnosisRequest(BaseModel):
    response_id: Optional[str] = Field(default=None, description="응답 ID")
    user_id: Optional[str] = Field(default=None, description="사용자 ID")
    submitted_at: Optional[str] = Field(default=None, description="제출 시각")
    q1: str
    q2: str
    q3: str
    q4: str
    q5: str
    q6: str
    q7: str
    q8: str
    q9: str
    q10: str
    q11: str
    q12: str
    q13: str
    q14: str
    q15: str
    q16: str
    q17: str
    q18: str
    q19: str
    q20: str
