def rotate(text, key):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cap_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    simple_sentence = list(text)
    for index,letter in enumerate(simple_sentence):
        if letter in letters:
            letters_index = letters.index(letter)
        elif letter in cap_letters:
            letters_index = cap_letters.index(letter)
        else:
            continue
        new_letters_index = (letters_index + key) % 26
        if letter in letters:
            simple_sentence[index] = letters[new_letters_index] 
        elif letter in cap_letters:
            simple_sentence[index] = cap_letters[new_letters_index] 
    return ''.join(simple_sentence)