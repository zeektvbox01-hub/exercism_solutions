def find_anagrams(word, candidates):
    word = word.lower()
    anagram_list = []
    for anagram in candidates:
        new_anagram = anagram.lower()
        if new_anagram == word:
            continue
        if sorted(word) == sorted(new_anagram):
            anagram_list.append(anagram)
    return anagram_list
    