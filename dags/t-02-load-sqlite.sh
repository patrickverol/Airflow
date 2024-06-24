#!/bin/bash

# Path to output file
OUTPUT_FILE="/opt/airflow/dags/output-data-capitalized.txt"

# Path to SQLite database
DATABASE="/opt/airflow/dags/dsa_p1.db"

# SQL command to create the table if it does not exist
SQL_CREATE="CREATE TABLE IF NOT EXISTS etl_dados (TIMESTAMP TEXT, VISITORID TEXT);"

# Create the table in the database (the database is created if it does not exist)
sqlite3 $DATABASE "$SQL_CREATE"

# Import the txt file and load the data into the table
sqlite3 $DATABASE <<EOF
.mode tabs
.separator "#"
.import $OUTPUT_FILE etl_dados
EOF

# Note:
# .mode tabs is a specific SQLite command that defines the display mode of queries
# .mode tabs configures SQLite to display results with tab-separated fields. This is useful for clearer formatting,
# especially when results are manipulated or redirected in shell scripts.