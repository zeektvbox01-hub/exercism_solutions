"""Decoder for a secret ... handhake?"""

ACTIONS_POSSIBLE = ["wink", "double blink", "close your eyes", "jump"]


def commands(binary_str: str)-> str:
    """Tells you the list of actions done for a certain number."""
    start,*rest = list(binary_str)
    actions = [ACTIONS_POSSIBLE[index] for index, value in enumerate(reversed(rest)) if value == "1"]
    if start == "1":
        actions.reverse()
    return actions