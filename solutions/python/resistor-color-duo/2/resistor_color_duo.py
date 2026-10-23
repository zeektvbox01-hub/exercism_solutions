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


def value(colours: list) -> int:
    """Returns the decoded resistor value."""
    return (COLOURS[colours[0]] * 10) + (COLOURS[colours[1]])
