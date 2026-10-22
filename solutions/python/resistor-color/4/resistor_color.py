"""Decodes a 1-color resistor"""

COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def color_code(color: str) -> int:
    """Returns the decoded color code"""
    return COLORS.index(color)


def colors() -> list[str]:
    """Return all colors"""
    return COLORS.copy()
