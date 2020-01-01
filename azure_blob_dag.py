"""
How to interact with Azure Blob Storage in Airflow
"""
from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.file_to_wasb import FileToWasbOperator
from airflow.contrib.operators.wasb_delete_blob_operator import WasbDeleteBlobOperator


default_args = {
    'owner': 'udacity',
    'start_date': '2019-12-30' ,
    'depends_on_past': False,
    'catchup': False
}

dag = DAG('Azure_Blob',
          default_args=default_args,
          description='upload and delete blobs (files) to/from Azure Blob Storage',
          schedule_interval='@monthly'
        )

# tasks definition 
start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

file_to_azure_blob = FileToWasbOperator(
    task_id='upload_azure_blob',
    dag=dag,
    file_path="/mnt/c/DAG/test.txt",
    container_name="airflow",
    blob_name="testblob.txt",
    wasb_conn_id="azure_blob"
)

delete_to_azure_blob = WasbDeleteBlobOperator(
    task_id='delete_azure_blob',
    dag=dag,
    wasb_conn_id="azure_blob",
    container_name="airflow",
    blob_name="Untitled-2.txt"    
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)


# tasks dependencies 
start_operator >> file_to_azure_blob
file_to_azure_blob >> delete_to_azure_blob
delete_to_azure_blob >> end_operator