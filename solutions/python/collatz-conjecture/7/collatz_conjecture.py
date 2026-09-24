""" This program looks for the number of steps for the Collatz Conjecture to occur"""

def steps(number: int) -> int:
    """ Calculates the number of steps it takes for the Collatz Conjecture to occur
    
    Parameters:
        number: The number to be tested

    Variables:
        loops: The number of steps it takes to reach 1
    
    Returns:
        The number of steps it takes to reach 1
    """
    loops = 0
    if number <= 0 :
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = (number * 3) + 1
        loops += 1
    return loops
        