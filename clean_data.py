
import pandas as pd

def clean_stock_data(filepath):
    df = pd.read_csv(filepath)

    # Convert date
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Drop rows with nulls
    df = df.dropna()

    # Sort by date
    df = df.sort_values('date')

    # Save cleaned version
    cleaned_path = filepath.replace('.csv', '_cleaned.csv')
    df.to_csv(cleaned_path, index=False)
    print(f"Cleaned data saved to: {cleaned_path}")

if __name__ == '__main__':
    clean_stock_data('../data/KO_1919-09-06_2025-04-17.csv')
