""""""

def square(number: int) -> int :
    """
    Finds the number of grains on a given square on a chessboard

    Parameters:
        number: The chessboard square that is given

    Returns:
        The grains on the given square
    
    """
    if number <= 0 or number >= 65:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total() -> int :
    """
    Finds the total number of grains that results from the Wheat and chessboard problem

    Returns:
        The amount of grains on the chessboard
    """
    return (2 ** 64) - 1
