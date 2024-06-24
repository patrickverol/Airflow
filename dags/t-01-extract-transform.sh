#!/bin/bash
# The line above is the shebang, which indicates that this script should be run in a bash shell.

# Print the string "etl-bash-airflow" to the terminal.
echo "etl-bash-airflow"

# Use the cut command to extract columns 1 and 4 from the input-data.txt file located in /opt/airflow/dags,
# delimited by '#', and redirects the output to output-data.txt in the same directory.
cut -f1,4 -d"#" /opt/airflow/dags/input-data.txt > /opt/airflow/dags/output-data.txt


# Use the tr command to convert all lowercase letters to uppercase
# from the contents of output-data.txt and redirects the output to output-data-capitalized.txt in the same directory.
tr "[a-z]" "[A-Z]" < /opt/airflow/dags/output-data.txt > /opt/airflow/dags/output-data-capitalized.txt


# Packs and compresses the output-data-capitalized.txt file into a tar.gz file called p1-log.tar.gz,
# storing in the /opt/airflow/dags directory.
tar -czvf /opt/airflow/dags/p1-log.tar.gz /opt/airflow/dags/output-data-capitalized.txt
