from __future__ import annotations

from datetime import datetime
from pathlib import Path
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

from src.pipeline.run_batch_diagnosis import run_batch


INPUT_CSV = str(PROJECT_ROOT / "data" / "raw" / "diagnosis_requests_example_aligned.csv")


def batch_job():
    run_batch(INPUT_CSV)


with DAG(
    dag_id="rule_based_learning_style_diagnosis",
    start_date=datetime(2026, 4, 1),
    schedule_interval=None,
    catchup=False,
    tags=["bat", "diagnosis", "rule-based"],
) as dag:
    diagnose_task = PythonOperator(
        task_id="run_rule_based_diagnosis",
        python_callable=batch_job,
    )
