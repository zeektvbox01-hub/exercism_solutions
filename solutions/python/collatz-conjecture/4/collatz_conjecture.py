""" This program looks for the number of steps for the Collatz Conjecture to occur"""

def steps(number):
    """ Calculates the number of steps it takes for the Collatz Conjecture to occur " " "
    
    Parameters:
        number(int or float): The number to be tested

    Variables:
        loops(int): The number of steps it takes to reach 1
    
    Returns:
        int: the number of steps it takes to reach 1
 
    Examples:
        >>> steps(15):
        25
        >>> bake_time_remaining(23):
        17
        
    The function starts by checking that the number is a positive integer greater than 0. It then defines the number as an 
    integer, then does the Collatz Conjecture. If the number is even, you divide it by 2. If the number is odd, you 
    multiply it by 3 and add 1. Repeat until you reach 1. The function then returns the steps it took to reach it.
    """
    loops = 0
    if number % 1 != 0 or number <= 0 :
        raise ValueError("Only positive integers are allowed")
    number = int(number)
    while number != 1:
        if number % 2 == 0:
            number //= 2
            loops += 1
        else:
            number = (number * 3) + 1
            loops += 1
    return loops
        