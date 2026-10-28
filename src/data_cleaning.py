import pandas as pd

def load_data(path):
    """Load the campaign dataset."""
    return pd.read_csv(path)

def clean_data(df):
    """Remove duplicates and fill missing values."""
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df