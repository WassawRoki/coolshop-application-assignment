from decimal import Decimal
def show_pretty_price(value: float):
    '''Input: Valuee (Price as a float) \n  \n Return: Rounded Price'''
    
    round_decider : float = Decimal(value) % 1
    if round_decider != 0:
        if round_decider < 0.50:
            return int(value) + 0.50
        elif round_decider > 0.50 and round_decider < 0.95:
            return int(value) + 0.95
        elif round_decider > 0.95:
            return int(value) + 1
        else:
            return value
    return value

