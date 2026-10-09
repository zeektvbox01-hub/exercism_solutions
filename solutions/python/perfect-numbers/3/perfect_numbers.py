import math

"Finds whether a number is perfect, abundant, or deficient"

def classify(number: int) -> str:
    """
    Returns the type of number based on the aliquot sum

    Parameters:
        number: The number given

    Returns:
        The catergory of the number
    """
    if number <= 0 :
        raise ValueError("Classification is only possible for positive integers.")
    square_number_range = math.isqrt(number)
    square_number = square_number_range
    if square_number ** 2 != number:
        square_number = 0
    factors = []
    for potential_factor in range(1,square_number_range + 1):
        if number % potential_factor == 0:
            if potential_factor != square_number:
                factors.append(number//potential_factor)
            factors.append(potential_factor)
    factors.sort()
    factors.pop(-1)
    total_sum = sum(factors)
    if total_sum == number:
        return "perfect"
    if total_sum > number:
        return "abundant"
    return "deficient"
    
