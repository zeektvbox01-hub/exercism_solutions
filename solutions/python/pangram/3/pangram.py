"""The pangram tester"""

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t','u','v','w','x','y','z']

def is_pangram(sentence: str) -> bool:
    """Returns whether a word is a pangram or not.

    Parameters:
    sentence: The sentence to be tested

    Returns:
        Is the word a pangram?
    """
    simple_sentence = sentence.lower()
    simple_sentence = ' '.join(simple_sentence)
    simple_sentence = simple_sentence.split()
    return all(letter in simple_sentence for letter in LETTERS)