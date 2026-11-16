def is_isogram(phrase):
    word = ""
    for letter in phrase:
        if letter.isalpha():
            word += letter.lower()
    return len(set(word)) == len(word)
