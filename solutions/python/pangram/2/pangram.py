import string
def is_pangram(sentence):
    return not any(x not in sentence.lower() for x in string.ascii_lowercase)