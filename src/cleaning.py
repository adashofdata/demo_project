import pandas as pd


def clean_name(text):
    """Turn a messy column name like ' Price ($) ' into 'price'."""
    text = text.strip().lower()
    text = text.replace('($)', '').strip()
    return text.replace(' ', '_')


def load_raw_data(path):
    """Read the raw CSV file. Never edit the raw file itself."""
    return pd.read_csv(path)


def clean_data(df):
    """Fix column names, drop incomplete rows and add a revenue column.

    Example: 2 Lattes at $4.50 -> revenue of 9.0
    """
    df = df.copy()  # don't change the original DataFrame
    df.columns = [clean_name(col) for col in df.columns]
    df = df.dropna()
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['quantity'] = df['quantity'].astype(int)
    df['revenue'] = df['price']
    return df
