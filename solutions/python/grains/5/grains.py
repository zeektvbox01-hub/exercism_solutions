"""Calculate grain amounts for the wheat and chessboard problem."""

NUMBER_OF_SQUARES = 64

def square(number: int) -> int:
    """
    Return the number of grains on the requested square.

    Parameters:
        number: The chessboard square that is given

    Returns:
        The grains on the given square
    
    """
    if not 1 <= number <= NUMBER_OF_SQUARES:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total() -> int :
    """
    Return the total number of grains on the chessboard.

    Returns:
        The amount of grains on the chessboard
    """
    return 2 ** NUMBER_OF_SQUARES - 1
