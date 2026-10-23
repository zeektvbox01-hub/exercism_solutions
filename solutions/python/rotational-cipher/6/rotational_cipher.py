"""Does the rotational cipher"""

import string

def rotate(text: str, key: int) -> str:
    """Returns rotated code.
    
    Parameters:
        text: The original text.
        key: The key to be shifted.

    Returns:
        The encoded code.
    """
    letters = string.ascii_lowercase
    new_key = letters[key:] + letters[:key]
    reference = str.maketrans(letters + letters.upper(), new_key + new_key.upper())
    return text.translate(reference)
