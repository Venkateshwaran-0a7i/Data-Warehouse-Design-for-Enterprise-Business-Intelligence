import sqlite3
import pandas as pd

def get_db_connection():
    db_path = r"d:\code\Python\Data warehouse design\data-warehouse-etl-bi\data\warehouse.db"
    return sqlite3.connect(db_path)

def load_warehouse_tables(conn):
    print("Loading data from staging to warehouse tables (Star Schema)...")
    
    # 1. Load Dimensions
    # Dim Geography
    conn.execute("INSERT OR IGNORE INTO dim_geography (geo_name) SELECT DISTINCT GEO FROM staging_retail_sales")
    
    # Dim Sales Type
    conn.execute("INSERT OR IGNORE INTO dim_sales_type (sales_description) SELECT DISTINCT Sales FROM staging_retail_sales")
    
    # Dim Date
    # Note: For SQLite we handle date components in Python or during load. 
    # Here we'll use a helper to populate dim_date from staging
    staging_df = pd.read_sql("SELECT DISTINCT REF_DATE FROM staging_retail_sales", conn)
    staging_df['year'] = staging_df['REF_DATE'].str.split('-').str[0].astype(int)
    staging_df['month'] = staging_df['REF_DATE'].str.split('-').str[1].astype(int)
    staging_df['quarter'] = (staging_df['month'] - 1) // 3 + 1
    staging_df.rename(columns={'REF_DATE': 'date_id'}, inplace=True)
    staging_df.to_sql('dim_date', conn, if_exists='append', index=False, method=None) # Using 'append' because of INSERT OR IGNORE logic in SQL is harder with to_sql
    # Actually, to be safe with 'INSERT OR IGNORE' logic in to_sql, we'll just clear and reload or use unique constraints
    
    # 2. Load Fact Table
    print("Populating fact_sales...")
    fact_query = """
    INSERT INTO fact_sales (date_id, geography_id, sales_type_id, sales_value)
    SELECT 
        s.REF_DATE,
        g.geography_id,
        st.sales_type_id,
        s.VALUE
    FROM staging_retail_sales s
    JOIN dim_geography g ON s.GEO = g.geo_name
    JOIN dim_sales_type st ON s.Sales = st.sales_description
    """
    conn.execute("DELETE FROM fact_sales") # Clear old facts if any for this demo
    conn.execute(fact_query)
    
    conn.commit()
    print("Warehouse tables loaded successfully.")

if __name__ == "__main__":
    conn = get_db_connection()
    load_warehouse_tables(conn)
    conn.close()
