def is_isogram(phrase):
    simple_sentence = phrase.lower()
    simple_sentence = ' '.join(simple_sentence)
    simple_sentence = simple_sentence.split()
    seen = set()
    duplicates = list(set([letter for letter in simple_sentence if letter in seen or seen.add(letter)]))
    if len(set(simple_sentence)) != len(simple_sentence):
        if duplicates == ['-']:
            return True
        return False
    return True