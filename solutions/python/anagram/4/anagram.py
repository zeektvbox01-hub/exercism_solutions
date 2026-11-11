def find_anagrams(word: str, candidates: list) -> list:
    lower_word = word.lower()
    anagram_list = []
    sorted_word = sorted(lower_word)
    for anagram in candidates:
        lower_anagram = anagram.lower()
        if sorted_word == sorted(lower_anagram) and lower_anagram != lower_word:
            anagram_list.append(anagram)
    return anagram_list
    