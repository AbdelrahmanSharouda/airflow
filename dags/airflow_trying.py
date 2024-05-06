from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime,timedelta

default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag',
    default_args=default_args,
    description='This is our first dag',
    start_date=datetime(2024, 5, 6, 2),
    schedule_interval='@daily'
    
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task!"
    )
    
    task1