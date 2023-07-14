from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from weather_api import weather_etl
import boto3
import botocore

BUCKET_NAME = 'weather-bucket-jaswanth' # replace with your bucket name
KEY = 'weather_data.csv' # replace with your object key

today = datetime.today()
d4 = today.strftime("%m_%d_%Y")
def s3_extract():
    s3 = boto3.resource('s3')

    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, f'weather_data_{today}')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise


dag_owner = 'jaswanth333'

default_args = {'owner': dag_owner,
        'depends_on_past': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=1)
        }

with DAG(
	dag_id="s3_extract",
    default_args=default_args,
	start_date=datetime(2023,6,29),
	schedule_interval=timedelta(days=1),
	catchup=False,
) as dag:

  download_csv = PythonOperator(
    	task_id="s3_extract_task",
    	python_callable=s3_extract)
   	 
  download_csv    