"""Decodes a two-band resistor"""

COLOURS = {
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
    }


def value(colours: list[str]) -> int:
    """Returns the decoded resistor value."""
    first_colour,second_colour = colours[0],colours[1]
    return (COLOURS[first_colour] * 10) + (COLOURS[second_colour])
