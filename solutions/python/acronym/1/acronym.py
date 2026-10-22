import string
import re

def abbreviate(words):
    words = re.sub(r"-"," ",words)
    words = words.replace("'","")
    words = words.title()
    acronym_list = []
    for letter in words:
        if letter not in string.ascii_uppercase:
            continue
        acronym_list.append(letter)
    return "".join(acronym_list)
        