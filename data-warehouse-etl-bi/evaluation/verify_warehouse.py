import sqlite3
import pandas as pd

def verify_warehouse():
    db_path = r"d:\code\Python\Data warehouse design\data-warehouse-etl-bi\data\warehouse.db"
    conn = sqlite3.connect(db_path)
    
    print("\n=== Data Warehouse Verification ===")
    
    # 1. Record Counts
    tables = ['staging_retail_sales', 'dim_geography', 'dim_sales_type', 'dim_date', 'fact_sales']
    print("\n--- Record Counts ---")
    for table in tables:
        count = pd.read_sql(f"SELECT COUNT(*) FROM {table}", conn).iloc[0,0]
        print(f"{table}: {count} rows")
        
    # 2. Sample Queries from the View
    print("\n--- Analytical Query: Total Sales by Geography (Top 5) ---")
    query1 = "SELECT geo_name, SUM(sales_value) as total_sales FROM view_sales_analysis GROUP BY geo_name ORDER BY total_sales DESC LIMIT 5"
    df1 = pd.read_sql(query1, conn)
    print(df1)
    
    print("\n--- Analytical Query: Total Sales by Year ---")
    query2 = "SELECT year, SUM(sales_value) as total_sales FROM view_sales_analysis GROUP BY year ORDER BY year"
    df2 = pd.read_sql(query2, conn)
    print(df2)
    
    conn.close()

if __name__ == "__main__":
    verify_warehouse()
