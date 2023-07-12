import pytest
from money_rounding import show_pretty_price

def test_show_pretty_price():
    # Test case 1:
    value = 10.25
    expected_output = 10.50
    assert show_pretty_price(value) == expected_output

    # Test case 2: 
    value = 15.75
    expected_output = 15.95
    assert show_pretty_price(value) == expected_output

    # Test case 3: 
    value = 20.80
    expected_output = 20.95
    assert show_pretty_price(value) == expected_output

    # Test case 4: 
    value = 30.50
    expected_output = 30.50
    assert show_pretty_price(value) == expected_output
    
    # Test case 5:
    value = 42.99
    expected_output = 43
    assert show_pretty_price(value) == expected_output
    
    # Test case 6:
    value = 19
    expected_output = 19
    assert show_pretty_price(value) == expected_output
    
    # Test case 7:
    value = 19.99
    expected_output = 20
    assert show_pretty_price(value) == expected_output