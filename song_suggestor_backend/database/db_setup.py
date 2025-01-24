import sqlite3

def execute_sql_file(conn, file_path):
    with open(file_path, 'r') as file:
        sql = file.read()
        conn.executescript(sql)

# Create a connection to the database
conn = sqlite3.connect("database/song_suggestor_demo.db")

# Load and execute DDL and data SQL files
execute_sql_file(conn, "resources/demo_ddl.sql")
execute_sql_file(conn, "resources/demo_data.sql")

# Commit changes and close the connection
conn.commit()
conn.close()