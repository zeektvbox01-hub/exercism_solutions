"""Checking for the Collatz Conjecture-but will it be possible?"""

def steps(number):
    "Looking for steps"
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
        