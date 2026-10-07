"""Pig Latin Translator"""

VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
VOWELS_SPECIAL = {"a", "e", "i", "o", "u", "y", "A","E", "I","O","U", "Y"}

def translate(text):
    """ Returns the Pig Latin Translation

    Parameters:
        text: The text provided in english

    Returns:
        The word in Pig Latin
"""
    translated_words = []
    for word in text.split(): 
        if word in VOWELS or word[:2].lower() in {"xr", "yt"}:
            translated_words.append(word + "ay")
            continue
        translated = False
        for index, char in enumerate(word):
            is_valid_vowel = char in VOWELS or (char in VOWELS_SPECIAL and index > 0)
            if is_valid_vowel:
                if char.lower() == "u" and index > 0 and word[index - 1].lower() == "q":
                    translated_words.append(word[index + 1:] + word[:index + 1] + "ay")
                else:
                    translated_words.append(word[index:] + word[:index] + "ay")
                translated = True
                break
        if not translated:
            translated_words.append(word + "ay")
    return " ".join(translated_words)
