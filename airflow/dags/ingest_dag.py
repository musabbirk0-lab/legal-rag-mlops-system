
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from app.ingest import ingest

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

dag = DAG('ingest_dag', default_args=default_args, schedule_interval='@daily')

ingest_task = PythonOperator(task_id='ingest_pdfs', python_callable=ingest, dag=dag)
