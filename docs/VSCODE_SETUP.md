# VS Code에서 처음부터 실행하기

## 1. 압축 풀기
1. zip 파일을 다운로드합니다.
2. 원하는 폴더에 압축을 풉니다.
3. `bat_rule_based_diagnosis_pipeline` 폴더가 생깁니다.

## 2. VS Code로 폴더 열기
1. VS Code 실행
2. `File -> Open Folder`
3. `bat_rule_based_diagnosis_pipeline` 선택

## 3. 터미널 열기
- 상단 메뉴 `Terminal -> New Terminal`

## 4. 가상환경 만들기
```bash
python -m venv .venv
```

## 5. 가상환경 켜기

### Windows PowerShell
```powershell
.\.venv\Scripts\Activate.ps1
```

### macOS / Linux
```bash
source .venv/bin/activate
```

## 6. 패키지 설치
```bash
pip install -r requirements.txt
```

## 7. 첫 배치 실행
```bash
python -m src.pipeline.run_batch_diagnosis --survey-csv-path data/raw/diagnosis_requests_example_aligned.csv
```

## 8. 결과 확인
- `data/processed/` 폴더에 결과 CSV가 생깁니다.

## 9. API 실행
```bash
uvicorn src.api.main:app --reload
```

브라우저 주소:
```text
http://127.0.0.1:8000/docs
```

## 10. Swagger 예시 입력
```json
{
  "response_id": "test_001",
  "user_id": "user_001",
  "submitted_at": "2026-04-09T20:00:00",
  "q1": "A",
  "q2": "B",
  "q3": "A",
  "q4": "A",
  "q5": "A",
  "q6": "A",
  "q7": "A",
  "q8": "A",
  "q9": "A",
  "q10": "A",
  "q11": "A",
  "q12": "B",
  "q13": "B",
  "q14": "B",
  "q15": "A",
  "q16": "A",
  "q17": "A",
  "q18": "A",
  "q19": "A",
  "q20": "A"
}
```
