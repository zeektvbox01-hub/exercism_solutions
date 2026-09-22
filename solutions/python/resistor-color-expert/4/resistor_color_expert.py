"""Resistor Colour Decoder"""

def resistor_label(colours: list) -> str:
    """Returns the amount of ohms and the tolerance
    
    Parameters:
    colours: The color code of the resistor

    Returns:
    The amount of ohms with the tolerance
    """
    ohms = 0
    tolerance = 0
    bands = len(colours)
    if bands == 1:
        return "0 ohms"
    if bands == 4:
        ohms = ((colour_code(colours[0]) * 10) + colour_code(colours[1])) * colour_code_powers(colours[2])
        tolerance = colour_code_resistance(colours[3])
        return final_string(ohms,tolerance)
    if bands == 5:
        ohms = int((colour_code(colours[0]) * 100 + colour_code(colours[1]) * 10 + colour_code(colours[2])) * colour_code_powers(colours[3]))
        tolerance = colour_code_resistance(colours[4])
        return final_string(ohms,tolerance)
        
def final_string(ohms,tolerance): 
    if ohms/1e9 >= 1:
        if (ohms/1e9).is_integer():
            return str(int(ohms/1e9)) + " gigaohms ±" + str(tolerance) + "%"
        return str(ohms/1e9) + " gigaohms ±" + str(tolerance) + "%"
    if ohms/1e6 >= 1:
        if (ohms/1e6).is_integer():
            return str(int(ohms/1e6)) + " megaohms ±" + str(tolerance) + "%"
        return str(ohms/1e6) + " megaohms ±" + str(tolerance) + "%"
    if ohms/1e3 >= 1:
        if (ohms/1e3).is_integer():
            return str(int(ohms/1e3)) + " kiloohms ±" + str(tolerance) + "%"
        return str(ohms/1e3) + " kiloohms ±" + str(tolerance) + "%"
    return str(ohms) + " ohms ±" + str(tolerance) + "%"
    
def colour_code(colour):
    return {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
    }.get(colour)

def colour_code_powers(colour):
    return {
    "black": 1,
    "brown": 10,
    "red": 100,
    "orange": 1000,
    "yellow": 1e4,
    "green": 1e5,
    "blue": 1e6,
    "violet": 1e7,
    "grey": 1e8,
    "white": 1e9,
    }.get(colour)

def colour_code_resistance(colour):
    return {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
    }.get(colour)