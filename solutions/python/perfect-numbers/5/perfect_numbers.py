"""Finds whether a number is perfect, abundant, or deficient"""

import math

def classify(number: int) -> str:
    """
    Returns the type of number based on the aliquot sum

    Parameters:
        number: The number given

    Returns:
        The catergory of the number
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    square_number = math.isqrt(number)
    factors = [1]
    for potential_factor in range(2,square_number + 1):
        if number % potential_factor == 0:
            factors.append(number//potential_factor)
            factors.append(potential_factor)
    factors.sort()
    total_sum = sum(set(factors))
    if number in factors:
        total_sum -= number
    if total_sum == number:
        return "perfect"
    if total_sum > number:
        return "abundant"
    return "deficient"
    
