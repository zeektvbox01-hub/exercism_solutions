"""Functions for creating, transforming, and adding prefixes to strings."""


import string

def add_prefix_un(word: str) -> str:
    """Take the given word and add the 'un' prefix.

    Parameters:
        word: The root word.

    Returns:
        Root word prepended with 'un'.
    """
    return "un" + word


def make_word_groups(vocab_words: list[str]) -> str:
    """Transform a list containing a prefix and words.

    Parameters:
        vocab_words: Vocabulary words with prefix at first index.

    Returns:
        Prefix followed by vocabulary words with the prefix applied.
    """
    return " :: ".join([vocab_words[0]] + [vocab_words[0] + word for word in vocab_words[1:]])


def remove_suffix_ness(word: str) -> str:
    """Remove the suffix from the word while keeping spelling in mind.

    Parameters:
        word: Word to remove suffix from.

    Returns:
        Word with suffix removed and spelling adjusted.
    """
    new_word = word.removesuffix("ness")
    if new_word.endswith("i"):
        new_word = new_word[:-1] + "y"
    return new_word


def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence: The word used in a sentence as an adjective.
        index: Index of the adjective to remove and transform.

    Returns:
        The extracted adjective in verb form.
    """
    main_word = sentence.split()[index].strip(string.punctuation)
    return main_word + "en"
