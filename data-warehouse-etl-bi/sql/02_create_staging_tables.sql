-- sql/02_create_staging_tables.sql
-- Drop staging tables if they exist
DROP TABLE IF EXISTS staging_retail_sales;

-- Create staging table based on raw data structure
CREATE TABLE staging_retail_sales (
    REF_DATE TEXT,
    GEO TEXT,
    DGUID TEXT,
    Sales TEXT,
    UOM TEXT,
    UOM_ID TEXT,
    SCALAR_FACTOR TEXT,
    SCALAR_ID TEXT,
    VECTOR TEXT,
    COORDINATE TEXT,
    VALUE REAL,
    STATUS TEXT,
    SYMBOL TEXT,
    TERMINATED TEXT,
    DECIMALS TEXT
);
