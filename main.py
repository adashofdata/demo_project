from pathlib import Path

from src.cleaning import load_raw_data, clean_data
from src.plotting import plot_revenue_by_drink

# build file paths starting from the folder this script is in
PROJECT_DIR = Path(__file__).parent
RAW_PATH = PROJECT_DIR / 'data' / 'raw' / 'coffee_sales.csv'
PROCESSED_PATH = PROJECT_DIR / 'data' / 'processed' / 'coffee_sales_clean.csv'
FIGURE_PATH = PROJECT_DIR / 'outputs' / 'revenue_by_drink.png'


def main():
    # 1. load
    df = load_raw_data(RAW_PATH)
    print(f'Loaded {len(df)} rows from data/raw')

    # 2. clean and save
    df = clean_data(df)
    PROCESSED_PATH.parent.mkdir(exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    print(f'Saved {len(df)} clean rows to data/processed')

    # 3. plot and save
    FIGURE_PATH.parent.mkdir(exist_ok=True)
    plot_revenue_by_drink(df, FIGURE_PATH)
    print('Saved chart to outputs')


if __name__ == '__main__':
    main()
