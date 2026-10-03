"""Finds if a number is a armstrong number"""

def is_armstrong_number(number:int) -> bool:
    """
    Checks if the given number is an Armstrong number.

    Parameters:
        number: The number given to check if it is an Armstrong number

    Returns:
        Is the number a armstrong number?
    
    """

    digits = [int(digit) for digit in str(number)]
    power = len(digits)
    return sum(digit ** power for digit in digits) == number