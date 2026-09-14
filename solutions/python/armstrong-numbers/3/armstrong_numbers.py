"""Moon to Earth. We have landed on the Moon, but an alien wants to see our math tricks. Please help!"""

def is_armstrong_number(number:int) -> bool:
    """
    Checks if the given number is an Armstrong number.

    Parameters:
        number: The number given to check if it is an Armstrong number

    Variables:
        digits: A list of the digits in the number
        digit_count: The number of digits in the number
        total_sum: The sum of the digits each raised to the power of the number of digits
        
    Returns:
        Whether the total sum is equal to the number
    
    """
    digits:list = [int(string_digits) for string_digits in str(number)]
    digit_count:int = len(str(number))
    total_sum: int = 0
    for string_digits in digits:
        total_sum += string_digits ** digit_count
    return total_sum == number