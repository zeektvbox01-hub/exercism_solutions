"""Isogram Finder"""


def is_isogram(phrase: str) -> bool:
    """Returns whether a word is a isogram or not

    Parameters:
        phrase: Phrase to be checked for isogram

    Returns:
        Is the word a isogram?
    """
    seen = set()
    for character in phrase.lower():
        if str.isalpha(character):
            if character in seen:
                return False
            seen.add(character)
    return True