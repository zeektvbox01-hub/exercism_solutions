"""Is this ISBN-10 valid? Check using this code"""

def is_valid(isbn: str) -> str:
    """Returns the validity of the ISBN

    Parameters:
        isbn: The ISBN-10 code to test

    Returns:
        Is this ISBN-10 valid?
    """
    isbn = isbn.replace('-', '')
    if len(isbn) != 10 or not isbn[:-1].isdigit():
        return False
    formula_result = 0
    for multiplier,number in enumerate(list(isbn)):
        new_number = number
        if multiplier == 9 and new_number == 'X':
            new_number = 10
        elif not number.isdigit():
            return False
        formula_result += (10 - multiplier) * int(new_number)
    return formula_result % 11 == 0
