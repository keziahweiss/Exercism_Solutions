import string
def is_pangram(sentence):
    for x in string.ascii_lowercase:
        if x not in sentence.lower():
            return False
    return True
