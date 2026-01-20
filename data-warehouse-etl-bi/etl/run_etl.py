import os
import sqlite3
from extract import extract_raw_data
from transform import transform_data
from load_staging import get_db_connection, execute_sql_file, load_to_staging
from load_warehouse import load_warehouse_tables

def run_pipeline():
    print("=== Starting Data Warehouse ETL Pipeline ===")
    
    # Configuration
    base_path = r"d:\code\Python\Data warehouse design\data-warehouse-etl-bi"
    raw_file = os.path.join(base_path, "data", "raw", "20100072.csv")
    sql_dir = os.path.join(base_path, "sql")
    
    # 1. Extraction
    df = extract_raw_data(raw_file)
    if df is None:
        return

    # 2. Transformation
    df_transformed = transform_data(df)
    
    # 3. Database & Schema Initialization
    conn = get_db_connection()
    
    print("Initializing Database Schema...")
    schema_files = [
        "02_create_staging_tables.sql",
        "03_create_dimensions.sql",
        "04_create_fact_tables.sql",
        "05_indexes_partitions.sql",
        "06_views_for_powerbi.sql"
    ]
    
    for f in schema_files:
        print(f"Executing {f}...")
        execute_sql_file(conn, os.path.join(sql_dir, f))
    
    # 4. Load Staging
    load_to_staging(df_transformed, conn)
    
    # 5. Load Warehouse (Star Schema)
    load_warehouse_tables(conn)
    
    # Cleanup
    conn.close()
    print("=== ETL Pipeline Completed Successfully ===")

if __name__ == "__main__":
    run_pipeline()
