# Pipeline for Extraction, Transformation and Loading into Database with Apache Airflow

# Imports
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta


# Defining the default arguments that will be applied to the DAG
default_args = {
    'owner': 'Patrick Verol',                       # Owner of DAG
    'start_date': days_ago(0),                      # DAG start date (current date)
    'email': ['your_email@gmail.com'],              # Email list for notifications
    'email_on_failure': False,                      # Disable email notifications in case of failure
    'email_on_retry': False,                        # Disable email notifications in case of a new attempt
    'retries': 1,                                   # Number of attempts in case of failure
    'retry_delay': timedelta(minutes=1),            # Time interval between attempts
}

# Link to cron reference: https://crontab.guru/

# Creating a DAG instance with the specified settings
dag_01 = DAG(
    'dag_01_etl_sh',                               # DAG identifier name
    default_args=default_args,                     # Applying the default arguments
    description='Project - Extraction of \
    txt file, Transformation and Load \
    in SQLite Bank',                               # Description of the DAG
    schedule_interval='15 22 * * *',               # Scheduling: Run daily at 22:15
    tags=['dag', 'etl']                            # Tags for DAG categorization and search
)

# Defining the first task using BashOperator
t1_extract_transform = BashOperator(
    task_id="t1_extract_transform",                # Unique identifier for the task
    bash_command="./t-01-extract-transform.sh",    # Bash command that will be executed by the task
    dag=dag_01,                                    # Associating the task with the DAG
)

# Defining the second task using BashOperator
t2_load_sqlite = BashOperator(
    task_id="t2_load_sqlite",                      # Unique identifier for the task
    bash_command="./t-02-load-sqlite.sh",          # Bash command that will be executed by the task
    dag=dag_01,                                    # Associating the task with the DAG
)

# Defining the task execution order: dsa_etl followed by insert_sqlite
t1_extract_transform >> t2_load_sqlite