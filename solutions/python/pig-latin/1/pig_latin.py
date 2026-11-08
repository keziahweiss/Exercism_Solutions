def translate_word(w):
    vowels = "aeiou"
    if w[0] in vowels or w.startswith(("xr", "yt")):
        w = w + "ay"
        return w
    for i, letter in enumerate(w):
        if w[i-1:i+1] == "qu":
            w = w[i+1:] + w[:i+1] + "ay"
            return w
        elif letter in vowels:
            w = w[i:] + w[:i] + "ay"
            return w
        elif letter == "y" and i != 0:
            w = w[i:] + w[:i] + "ay"
            return w

def translate(text):
    words = text.split()
    result = []
    for w in words:
        result.append(translate_word(w))
    return " ".join(result)
