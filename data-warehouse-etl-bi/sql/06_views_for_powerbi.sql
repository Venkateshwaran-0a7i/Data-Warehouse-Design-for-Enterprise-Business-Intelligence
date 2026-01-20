-- sql/06_views_for_powerbi.sql
-- View for BI tools
DROP VIEW IF EXISTS view_sales_analysis;
CREATE VIEW view_sales_analysis AS
SELECT 
    f.sales_value,
    d.year,
    d.month,
    d.quarter,
    g.geo_name,
    s.sales_description
FROM fact_sales f
JOIN dim_date d ON f.date_id = d.date_id
JOIN dim_geography g ON f.geography_id = g.geography_id
JOIN dim_sales_type s ON f.sales_type_id = s.sales_type_id;
