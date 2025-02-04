import os
from dotenv import load_dotenv
load_dotenv()

from airflow.models.dag import DAG
import pendulum

from airflow.operators.bash import (
    BashOperator
)

with DAG(
    dag_id="dag_my_anime_list_api",
    schedule=None,
    start_date=pendulum.datetime(2024, 9, 16, tz="UTC"),
    catchup=False
):
    get_data_from_api = BashOperator(
        task_id = 'get_data_from_api',
        bash_command = f"python3 {os.getenv('PYTHON_DIRECTORY')}/get_data_from_api.py"
    )
    
    
get_data_from_api