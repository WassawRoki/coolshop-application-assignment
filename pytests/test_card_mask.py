import pytest
from card_masks import get_card_mask

def test_get_card_mask():
    # Test case 1: Masking Visa card
    card_type = "Visa"
    card_number = "1234567890123456"
    expected_output = "VISA1234xxxxxxxx3456"
    assert get_card_mask(card_type, card_number) == expected_output

    # Test case 2: Masking Mastercard
    card_type = "Mastercard"
    card_number = "9876543210987654"
    expected_output = "MASTERCARD9876xxxxxxxx7654"
    assert get_card_mask(card_type, card_number) == expected_output

    # Test case 3: Masking American Express card
    card_type = "American Express"
    card_number = "1111222233334444"
    expected_output = "AMERICAN EXPRESS1111xxxxxxxx4444"
    assert get_card_mask(card_type, card_number) == expected_output

    # Test case 4: Masking Coolshop membership card
    card_type = "CoolMember"
    card_number = "5555666677778888"
    expected_output = "COOLMEMBER5555xxxxxxxx8888"
    assert get_card_mask(card_type, card_number) == expected_output