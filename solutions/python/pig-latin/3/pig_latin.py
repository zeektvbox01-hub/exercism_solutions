"""Igpay Atinlay Anslatortray"""

VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
VOWELS_SPECIAL = {"a","e","i","o","u","y","A","E","I","O","U","Y",}

def translate(text):
    """
    Ifay aay ordway artsstay ithway oneway oray oremay onsonantscay ollowedfay ybay 'yway', irstfay ovemay ethay onsonantscay ecedingpray ethay 'yway'toay ethay enday ofay ethay ordway, anday enthay adday anay 'ayay' oundsay toay ethay enday ofay ethay ordway.
    
    Ifay aay ordway eginsbay ithway oneway oray oremay onsonantscay, irstfay ovemay osethay onsonantscay toay ethay enday ofay ethay ordway anday enthay adday anay 'ayay' oundsay toay ethay enday ofay ethay ordway.

Ifay aay ordway artsstay ithway erozay oray oremay onsonantscay ollowedfay ybay 'uquay', irstfay ovemay osethay onsonantscay (ifay anyay) anday ethay 'uquay' artpay toay ethay enday ofay ethay ordway, anday enthay adday anay 'ayay' oundsay toay ethay enday ofay ethay ordway.

Ifay aay ordway artsstay ithway oneway oray oremay onsonantscay ollowedfay ybay 'yway', irstfay ovemay ethay onsonantscay ecedingpray ethay 'yway' toay ethay enday ofay ethay ordway, anday enthay adday anay 'ayay' oundsay toay ethay enday ofay ethay ordway.
"""
    translated_words = []
    for word in text.split():
        if word in VOWELS or word[:2].lower() in {'xr', 'yt'}:
            translated_words.append(word + "ay")
            continue
        translated = False
        for index, char in enumerate(word):
            is_valid_vowel = char in VOWELS or (char in VOWELS_SPECIAL and index > 0)
            if is_valid_vowel:
                if char.lower() == "u" and index > 0 and word[index-1].lower() == "q":
                    translated_words.append(word[index+1:] + word[:index+1] + "ay")
                else:
                    translated_words.append(word[index:] + word[:index] + "ay")
                translated = True
                break
        if not translated:
            translated_words.append(word + "ay")
    return " ".join(translated_words)
