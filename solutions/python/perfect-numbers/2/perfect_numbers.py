"Finds whether a number is perfect, abundant, or deficient"

def classify(number: int) -> str:
    """
    Returns the type of number based on the aliquot sum

    Parameters:
        number:The number given

    Returns:
        The catergory of the number
    """
    if number % 1 != 0 or number <= 0 :
        raise ValueError("Classification is only possible for positive integers.")
    factors = [factor for factor in range(1, number) if number % factor == 0]
    total_sum = 0
    for factor in factors:
        total_sum += factor
    if total_sum == number:
        return "perfect"
    if total_sum > number:
        return "abundant"
    return "deficient"
    
