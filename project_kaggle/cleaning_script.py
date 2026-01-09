"""Simple cleaning script for Kaggle project.
Usage: python cleaning_script.py input.csv output.csv
"""
import sys
import pandas as pd

def clean(infile, outfile):
    df = pd.read_csv(infile)
    # Trim whitespace from column names
    df.columns = [c.strip() for c in df.columns]
    # Drop rows that are entirely empty
    df = df.dropna(how='all')
    # Drop exact duplicate rows
    df = df.drop_duplicates()
    # Example: standardize datetime columns if present
    for col in df.columns:
        if 'date' in col.lower() or 'time' in col.lower():
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass
    df.to_csv(outfile, index=False)
    print(f"Saved cleaned data to {outfile}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python cleaning_script.py input.csv output.csv')
    else:
        clean(sys.argv[1], sys.argv[2])
