"""Finds what bob would say"""

def response(hey_bob: str) -> str:
    """Returns the response of Bob.

    Parameters:
        hey_bob: What a person says to Bob

    Returns:
        What Bob replies to the person.
        
    """
    hey_bob = hey_bob.strip()
    if hey_bob == "":
        return "Fine. Be that way!"
    if hey_bob[-1] == "?":
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."
