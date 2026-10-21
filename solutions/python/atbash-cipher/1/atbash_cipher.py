import string

def encode(plain_text):
    letters = string.ascii_lowercase
    new_key = letters[::-1]
    reference = str.maketrans(letters + letters.upper(), new_key + new_key.upper(),string.punctuation)
    new_text = plain_text.lower().translate(reference)
    new_text = new_text.replace(" ","")
    final_text = []
    for number in range(0, len(new_text),5):
        final_text.append(new_text[number: number + 5])
    return " ".join(final_text)

def decode(ciphered_text):
    new_key = string.ascii_lowercase
    letters = new_key[::-1]
    reference = str.maketrans(letters, new_key)
    old_text = ciphered_text.lower().translate(reference)
    return old_text.replace(" ","")
