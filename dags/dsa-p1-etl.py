# Projeto 1 - Pipeline de Extração, Transformação e Carga em Banco de Dados com Apache Airflow

# Imports
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

# Definindo os argumentos padrões que serão aplicados à DAG
default_args = {
    'owner': 'Data Science Academy',                # Proprietário da DAG
    'start_date': days_ago(0),                      # Data de início da DAG (data atual)
    'email': ['suporte@datascienceacademy.com.br'], # Lista de emails para notificações
    'email_on_failure': False,                      # Desativa notificações por email em caso de falha
    'email_on_retry': False,                        # Desativa notificações por email em caso de nova tentativa
    'retries': 1,                                   # Número de tentativas em caso de falha
    'retry_delay': timedelta(minutes=1),            # Intervalo de tempo entre tentativas
}

# Link para referência sobre cron: https://crontab.guru/

# Criando uma instância de DAG com as configurações especificadas
dsa_dag = DAG(
    'dsa_p1_etl',                                  # Nome identificador da DAG
    default_args=default_args,                     # Aplicando os argumentos padrões
    description='Projeto 1',                       # Descrição da DAG
    schedule_interval='15 22 * * *',               # Agendamento: Executar diariamente às 22:15
    tags=['dsa', 'etl']                            # Tags para categorização e busca da DAG
)

# Definindo a primeira tarefa usando BashOperator
dsa_etl = BashOperator(
    task_id="dsa_etl",                             # Identificador único para a tarefa
    bash_command="./dsa-p1-etl.sh",                # Comando bash que será executado pela tarefa
    dag=dsa_dag,                                   # Associando a tarefa à DAG
)

# Definindo a segunda tarefa usando BashOperator
insert_sqlite = BashOperator(
    task_id="insert_sqlite",                       # Identificador único para a tarefa
    bash_command="./dsa-p1-insert-sqlite.sh",      # Comando bash que será executado pela tarefa
    dag=dsa_dag,                                   # Associando a tarefa à DAG
)

# Definindo a ordem de execução das tarefas: dsa_etl seguido por insert_sqlite
dsa_etl >> insert_sqlite


