<br>
  <h1 align="center">
    ETL using Apache Airflow, bash script, SQLite and Docker
  </h1>
  <h1 align="center">
    ![project-airflow](https://github.com/patrickverol/Airflow/assets/102604896/c09f111f-12bf-4771-81cc-d18e8f5fa691)
  </h1>
<br/>

<div align="center">
    <a href = "https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" target="_blank"></a> 
    <a href = "https://airflow.apache.org/docs/"><img src="https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white" target="_blank"></a>
    <a href = "https://docs.docker.com/"><img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" target="_blank"></a>
    <a href = "https://www.sqlite.org/docs.html"><img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white" target="_blank"></a>
</div> 

## About the project

In this project, an ETL process will be carried out, with data extraction from a CSV file, transformation using a bash script, and loading into an SQLite database. The entire process is orchestrated by Apache Airflow, where the task can be scheduled to run at any time you want.

## Installation and configuration

  1. Clone the repository in the folder you want.

```bash
  git clone https://github.com/patrickverol/Airflow
```
  2. Open the terminal or command prompt and navigate to the folder where the files are.

```bash
  cd your_folder
```
  3. Run the command below to create the Airflow Docker images and initialize the database.
```bash
  docker compose up airflow-init
```
  4. Run the command below to initialize Airflow.

```bash
  docker compose up
```
  5. Open the browser and log in.
```bash
  http://localhost:8080/login

    User: airflow
    Senha: airflow
```
Note: If you have PostgreSQL installed on your machine running on port 5432, turn it off or there will be a port conflict preventing Airflow from starting.

## Contact

For questions, suggestions or feedback:

<div>
    <a href="https://www.linkedin.com/in/patrick-verol/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
    <a href = "mailto:patrickverol@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div> 
