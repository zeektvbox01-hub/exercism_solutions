def rotate(text, key):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cap_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    simple_sentence = '*'.join(text)
    simple_sentence = simple_sentence.split('*')
    for index,letter in enumerate(simple_sentence):
        if letter in letters:
            letters_index = letters.index(letter)
            new_letters_index = letters_index + key 
            new_letters_index = new_letters_index % 26
            simple_sentence[index] = letters[new_letters_index] 
        elif letter in cap_letters:
            cap_letters_index = cap_letters.index(letter)
            new_cap_letters_index = cap_letters_index + key 
            new_cap_letters_index = new_cap_letters_index % 26
            simple_sentence[index] = cap_letters[new_cap_letters_index] 
    return ''.join(simple_sentence)