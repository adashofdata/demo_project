import pandas as pd
from src.cleaning import clean_name, clean_data


def test_clean_name_removes_dollar_sign():
    assert clean_name(' Price ($) ') == 'price'


def test_clean_name_replaces_spaces():
    assert clean_name('Order Date') == 'order_date'

def test_clean_data_adds_revenue():
    # arrange
    df = pd.DataFrame({'Order Date': ['2026-09-01'], ' Drink ': ['Latte'],
                       'Size': ['L'], 'Price ($)': [4.50], 'Quantity': [2]})

    # act
    result = clean_data(df)

    # assert
    assert result['revenue'].iloc[0] == 9.0