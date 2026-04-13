# 파이프라인 구조

입력 CSV/API -> normalize -> score -> result text attach -> save/return

## 파일별 역할
- `question_rules.py`
  - q1~q20 문항 규칙표
- `normalize.py`
  - A/B, 0/1, 한글 응답을 trait로 통일
- `scoring.py`
  - 네 가지 점수 계산
- `result_mapper.py`
  - 검사결과지 문구를 유형별로 붙임
- `run_batch_diagnosis.py`
  - CSV 일괄 처리
- `main.py`
  - FastAPI 서버
