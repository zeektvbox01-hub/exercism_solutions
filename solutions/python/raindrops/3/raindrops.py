"""Convert numbers into sounds"""

def convert(number: int) -> str:
    """Return the raindrop sounds associated with a number.

    Parameters:
        number: The number given to be converted

    Returns:
        The converted number as a string
    """
    final_string = ""
    if number % 3 == 0:
        final_string = final_string + "Pling"
    if number % 5 == 0:
        final_string = final_string + "Plang"
    if number % 7 == 0:
        final_string = final_string + "Plong"
    if not final_string:
        final_string = str(number)
    return final_string
