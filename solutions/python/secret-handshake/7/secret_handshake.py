"""Decoder for a secret ... handhake?"""

ACTIONS_POSSIBLE = ["wink", "double blink", "close your eyes", "jump"]


def commands(binary_str):
    """Tells you the list of actions done for a certain number."""
    actions = [ACTIONS_POSSIBLE[index] for index, value in enumerate(reversed(binary_str[1:])) if value == "1"]
    if binary_str[0] == "1":
        actions.reverse()
    return actions