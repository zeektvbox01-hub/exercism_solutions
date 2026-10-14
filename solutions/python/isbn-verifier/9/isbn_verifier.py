"""Is this ISBN-10 valid? Check using this code"""

NUMBERS = ['0','1','2','3','4','5','6','7','8','9']

def is_valid(isbn: str) -> str:
    """Returns the validity of the ISBN

    Parameters:
        isbn: The ISBN-10 code to test

    Returns:
        Is this ISBN-10 valid?
    """
    isbn = isbn.replace('-', '')
    if any([len(list(isbn)) != 10,list(isbn).count('X') > 1,not isbn[:-1].isdigit()]):
        return False
    formula_result = 0
    for multiplier,number in enumerate(list(isbn)):
        if multiplier == 9 and number == 'X':
            number = 10
        elif multiplier == 9 and number not in NUMBERS:
            return False
        formula_result += (10 - multiplier) * int(number)
    return formula_result % 11 == 0
