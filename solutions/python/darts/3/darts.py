"""Finds scores for dart throws."""

import math

def score(coordinate_x: int, coordinate_y: int) -> str:
    """Returns the score based on its coordinates

    Parameters:
        coordinate_x: Its location on the x axis
        coordinate_y: Its location on the y axis

    Returns:
        The score obtained 
    """
    distance = math.sqrt(coordinate_x ** 2 + coordinate_y ** 2)
    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    return 0