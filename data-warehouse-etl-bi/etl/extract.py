import pandas as pd
import os

def extract_raw_data(file_path):
    """Extract data from a raw CSV file."""
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return None
    
    print(f"Extracting data from {file_path}...")
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    # Example usage for testing
    raw_file = r"d:\code\Python\Data warehouse design\data-warehouse-etl-bi\data\raw\20100072.csv"
    data = extract_raw_data(raw_file)
    if data is not None:
        print(f"Extraction successful. Rows: {len(data)}")
        print(data.head())
