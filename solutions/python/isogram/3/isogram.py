"""Isogram Finder"""
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t','u','v','w','x','y','z']


def is_isogram(phrase: str) -> bool:
    """Returns whether a word is a isogram or not

    Parameters:
        phrase: Phrase to be checked for isogram

    Returns:
        Is the word a isogram?
    """
    simple_sentence = phrase.lower()
    simple_sentence = '_'.join(simple_sentence)
    letters_list = simple_sentence.split('_')
    seen = []
    for letter in letters_list:
        if letter not in LETTERS:
            continue
        try:
            seen.index(letter)
            return False
        except ValueError:
            seen.append(letter)
    return True