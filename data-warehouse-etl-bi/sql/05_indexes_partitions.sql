-- sql/05_indexes_partitions.sql
-- Create indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_fact_date ON fact_sales(date_id);
CREATE INDEX IF NOT EXISTS idx_fact_geography ON fact_sales(geography_id);
CREATE INDEX IF NOT EXISTS idx_fact_sales_type ON fact_sales(sales_type_id);

CREATE INDEX IF NOT EXISTS idx_dim_geo_name ON dim_geography(geo_name);
CREATE INDEX IF NOT EXISTS idx_dim_sales_desc ON dim_sales_type(sales_description);
