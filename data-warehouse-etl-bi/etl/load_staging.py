import sqlite3
import pandas as pd
import os

def get_db_connection():
    db_path = r"d:\code\Python\Data warehouse design\data-warehouse-etl-bi\data\warehouse.db"
    conn = sqlite3.connect(db_path)
    return conn

def execute_sql_file(conn, sql_file_path):
    with open(sql_file_path, 'r') as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()

def load_to_staging(df, conn):
    print("Loading data to staging...")
    df.to_sql('staging_retail_sales', conn, if_exists='replace', index=False)
    print("Data loaded to staging table.")

if __name__ == "__main__":
    from extract import extract_raw_data
    raw_file = r"d:\code\Python\Data warehouse design\data-warehouse-etl-bi\data\raw\20100072.csv"
    df = extract_raw_data(raw_file)
    if df is not None:
        conn = get_db_connection()
        # Initialize schema if needed
        sql_script = r"d:\code\Python\Data warehouse design\data-warehouse-etl-bi\sql\02_create_staging_tables.sql"
        execute_sql_file(conn, sql_script)
        load_to_staging(df, conn)
        conn.close()
