"""Does the rotational cipher"""

import string

def rotate(text, key):
    """Returns rotated code 
    
    Parameters:
        text
        
    """
    letters = string.ascii_lowercase
    new_key = letters[key:] + letters[:key]
    reference = str.maketrans(letters + letters.upper(), new_key + new_key.upper())
    return text.translate(reference)