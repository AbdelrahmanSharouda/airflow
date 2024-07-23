from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta

default_args = {
    'owner': 'abdelrahman',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def greet():
    print('Hello World!')

with DAG(
    dag_id='our_first_dag_v4',
    default_args=default_args,
    description='This is our first dag',
    start_date=datetime(2024, 5, 6, 2),
    schedule_interval='@daily'
        
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task!"
    )
    
    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo hey, I am task2 and will be running after task1"
    )
    
    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo hey, running in the samme time as task2"
    )
    
    task4 = PythonOperator(
        task_id='fourth_task',
        python_callable=greet
    )
    
    task1 >> task2
    task1 >> task3 >> task4