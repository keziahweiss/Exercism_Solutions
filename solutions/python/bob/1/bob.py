def response(hey_bob):
    hey_bob = hey_bob.strip()
    question = hey_bob.endswith("?")
    silence = hey_bob == ""
    yelling = hey_bob.isupper()
    if silence:
        return "Fine. Be that way!"
    elif yelling and question:
        return "Calm down, I know what I'm doing!"
    elif question:
        return "Sure."
    elif yelling:
        return "Whoa, chill out!"
    else:
        return "Whatever."