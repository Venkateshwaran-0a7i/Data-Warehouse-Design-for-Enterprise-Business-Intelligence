-- sql/03_create_dimensions.sql
-- Dimension: Geography
DROP TABLE IF EXISTS dim_geography;
CREATE TABLE dim_geography (
    geography_id INTEGER PRIMARY KEY AUTOINCREMENT,
    geo_name TEXT UNIQUE
);

-- Dimension: Sales Type (Sales category from raw data)
DROP TABLE IF EXISTS dim_sales_type;
CREATE TABLE dim_sales_type (
    sales_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sales_description TEXT UNIQUE
);

-- Dimension: Date
DROP TABLE IF EXISTS dim_date;
CREATE TABLE dim_date (
    date_id TEXT PRIMARY KEY, -- Format: YYYY-MM
    year INTEGER,
    month INTEGER,
    quarter INTEGER
);
