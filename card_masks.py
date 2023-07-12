
def get_card_mask(card_type : str, card_number : str):
    '''Input: Card Type (Name of card type) \n Input: Card_Number (Serial Number of Card) \n Return: Masked Card Info (Card Type and Number Masked)'''
    
    if card_number.isnumeric() or len(card_number) != 16:
        temp_mask : str = ""
        
        #Iterates through the card number and maskes identifying numbers
        for i in  range(len(card_number)):
            if i >= 4 and i < len(card_number)-4:
                temp_mask += "x"
            else:
                temp_mask += card_number[i]
        
        #Ensures the card type is uppercase, and adds the masked number
        card_mask = card_type.upper() + temp_mask
    else:
        raise InvalidCardNumberException("Invalid card number length. Expected 16 digits.")
    
    return card_mask


class InvalidCardNumberException(Exception):
    #Extend to have diffrent exceptions wether it is wrong lenght, or contains ilegal symbols.
    pass


