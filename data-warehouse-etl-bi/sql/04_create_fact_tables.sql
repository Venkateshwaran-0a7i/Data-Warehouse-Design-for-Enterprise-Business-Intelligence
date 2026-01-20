-- sql/04_create_fact_tables.sql
-- Fact: Sales
DROP TABLE IF EXISTS fact_sales;
CREATE TABLE fact_sales (
    fact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_id TEXT,
    geography_id INTEGER,
    sales_type_id INTEGER,
    sales_value REAL,
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY (geography_id) REFERENCES dim_geography(geography_id),
    FOREIGN KEY (sales_type_id) REFERENCES dim_sales_type(sales_type_id)
);
