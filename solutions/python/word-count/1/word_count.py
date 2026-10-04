import re

def count_words(sentence):
    simple_sentence = sentence.lower()
    simple_sentence = re.split(r"""[,!&@$%^:."_]|\s+""",simple_sentence)
    words = {}
    for word in simple_sentence:
        new_word = word.strip("'")
        try:
            words[new_word] += 1
            continue
        except KeyError:
            words[new_word] = 1
    try:
        words.pop("")
    except KeyError:
        pass
    return words