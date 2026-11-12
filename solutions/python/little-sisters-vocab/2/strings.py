"""Functions for creating, transforming, and adding prefixes to strings."""

def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.
    Parameters:
        word (str): The root word.
    Returns:
        str: Root word prepended with 'un'.
    """
    word = "un" + word
    return word

def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words.
    Parameters:
        vocab_words (list[str]): Vocabulary words with prefix at first index.
    Returns:
        str: Prefix followed by vocabulary words with prefix applied.
    This function takes a `vocab_words` list of strings and returns a string
    with the prefix and the words with prefix applied, separated by ' :: '.
    """
    prefix = " :: " + vocab_words[0]
    prefix_list = prefix.join(vocab_words)
    return prefix_list

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.
    Parameters:
        word (str): Word to remove suffix from.
    Returns:
        str: Word with suffix removed & spelling adjusted.
    """
    word = word[:-4]
    if word[-1] == "i":
        word = word[:-1] + "y"
    return word

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.
    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.
    Returns:
        str: The extracted adjective in verb form.
    """
    words = sentence.split()
    adjective = words[index].strip(".")
    return adjective + "en"