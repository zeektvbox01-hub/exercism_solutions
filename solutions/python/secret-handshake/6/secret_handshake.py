"""Decoder for a secret ... handhake?"""

ACTIONS_POSSIBLE = ["wink", "double blink", "close your eyes", "jump"]


def commands(binary_str):
    """Tells you the list of actions done for a certain number"""
    actions = []
    for index, value in enumerate(reversed(binary_str)):
        if value == "1":
            if index == 4:
                actions.reverse()
            else:
                actions.append(ACTIONS_POSSIBLE[index])
    return actions