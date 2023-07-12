import pytest
from delivery_calculator import get_delivery_date

def test_get_delivery_date():
    from datetime import datetime, timezone
    expected = "2021, 05, 21"
    
    value = get_delivery_date(datetime(2021, 5, 20, 12, 51, 32, 199883, tzinfo=timezone.utc))
    
    assert value == expected

    assert get_delivery_date(datetime(2021, 5, 21, 13, 3, 31, 245381, tzinfo=timezone.utc)) == "2021, 05, 25"

    assert get_delivery_date(datetime(2020, 12, 29, 12, 15, 12, 0, tzinfo=timezone.utc)) == "2020, 12, 30"

    assert get_delivery_date(datetime(2020, 12, 29, 14, 15, 12, 0, tzinfo=timezone.utc)) == "2021, 01, 04"
