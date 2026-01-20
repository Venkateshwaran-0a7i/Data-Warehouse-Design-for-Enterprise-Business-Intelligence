import pandas as pd

def transform_data(df):
    """Transform raw data into a cleaned format suitable for star schema."""
    print("Starting data transformation...")
    
    # Clean column names (strip whitespace)
    df.columns = [c.strip() for c in df.columns]
    
    # 1. Clean VALUE column (handle non-numeric values if any, although raw sample looked numeric)
    # Ensure VALUE is float
    df['VALUE'] = pd.to_numeric(df['VALUE'], errors='coerce')
    
    # 2. Extract Date Components from REF_DATE (Format: YYYY-MM)
    df['REF_DATE'] = df['REF_DATE'].astype(str)
    df['year'] = df['REF_DATE'].str.split('-').str[0].astype(int)
    df['month'] = df['REF_DATE'].str.split('-').str[1].astype(int)
    df['quarter'] = (df['month'] - 1) // 3 + 1
    
    # 3. Rename columns for clarity if needed
    # (Mapping GEO to geography, Sales to sales_type)
    
    print("Transformation complete.")
    return df

def generate_dimensions(df):
    """Generate dimension tables from the transformed dataframe."""
    dim_geography = df[['GEO']].drop_duplicates().reset_index(drop=True)
    dim_sales_type = df[['Sales']].drop_duplicates().reset_index(drop=True)
    
    dim_date = df[['REF_DATE', 'year', 'month', 'quarter']].drop_duplicates().reset_index(drop=True)
    dim_date.rename(columns={'REF_DATE': 'date_id'}, inplace=True)
    
    return dim_geography, dim_sales_type, dim_date

if __name__ == "__main__":
    # Test block
    from extract import extract_raw_data
    raw_file = r"d:\code\Python\Data warehouse design\data-warehouse-etl-bi\data\raw\20100072.csv"
    raw_df = extract_raw_data(raw_file)
    if raw_df is not None:
        transformed_df = transform_data(raw_df)
        geo, sales, dt = generate_dimensions(transformed_df)
        print(f"Unique Geographies: {len(geo)}")
        print(f"Unique Sales Types: {len(sales)}")
        print(f"Unique Dates: {len(dt)}")
