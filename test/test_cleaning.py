from src.cleaning import clean_name


def test_clean_name_removes_dollar_sign():
    assert clean_name(' Price ($) ') == 'price'


def test_clean_name_replaces_spaces():
    assert clean_name('Order Date') == 'order_date'