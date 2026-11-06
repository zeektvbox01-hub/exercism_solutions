def find_anagrams(word, candidates):
    lower_word = word.lower()
    anagram_list = []
    sorted_word = sorted(lower_word)
    for anagram in candidates:
        new_anagram = anagram.lower()
        if sorted_word == sorted(new_anagram) and new_anagram != lower_word:
            anagram_list.append(anagram)
    return anagram_list
    