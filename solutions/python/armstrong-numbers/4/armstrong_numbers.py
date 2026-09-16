"""Finds if a number is a armstrong number"""

def is_armstrong_number(number:int) -> bool:
    """
    Checks if the given number is an Armstrong number.

    Parameters:
        number: The number given to check if it is an Armstrong number

    Returns:
        Is the number a armstrong number?
    
    """
    digits = [int(string_digits) for string_digits in str(number)]
    digit_count = len(str(number))
    total_sum = 0
    for string_digits in digits:
        total_sum += string_digits ** digit_count
    return total_sum == number