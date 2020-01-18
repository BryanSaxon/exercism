import string

def is_pangram(sentence):
    alphabet = string.ascii_letters[0:26]

    for letter in alphabet:
        if letter not in sentence.lower(): return False

    return True

