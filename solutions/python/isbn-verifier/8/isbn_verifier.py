"""Is this ISBN-10 valid? Check using this code"""

NUMBERS = ['0','1','2','3','4','5','6','7','8','9']

def is_valid(isbn: str) -> str:
    """Returns the validity of the ISBN

    Parameters:
        isbn: The ISBN-10 code to test

    Returns:
        Is this ISBN-10 valid?
    """
    isbn = list(isbn.replace('-', ''))
    if len(isbn) != 10:
        return False
    for index,key in enumerate(isbn):
        if key == 'X':
            if isbn[9] != 'X':
                return False
            isbn[9] = 10
        elif key not in NUMBERS:
            return False
    for index,key in enumerate(isbn):
        isbn[index] = int(key)
    formula_result = 0
    for multiplier,number in enumerate(isbn):
        formula_result += (10 - multiplier) * number
    return formula_result % 11 == 0
