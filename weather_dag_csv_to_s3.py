from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from weather_api import weather_etl
import s3fs

dag_owner = 'jaswanth333'

default_args = {'owner': dag_owner,
        'depends_on_past': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=1)
        }

with DAG(
    default_args=default_args,
    dag_id='API_CSV_S3',
    description='Call data from API and store csv data in s3',
    start_date=datetime(2023, 7,13),
    schedule_interval='@daily'
) as dag:
    upload_data=PythonOperator(
        task_id='upload_csv_to_s3',
        python_callable=weather_etl,
    )
    
    
    upload_data