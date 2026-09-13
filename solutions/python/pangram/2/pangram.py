def is_pangram(sentence):
    simple_sentence = sentence.lower()
    letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    simple_sentence = ' '.join(simple_sentence)
    simple_sentence = simple_sentence.split()
    return all(letter in simple_sentence for letter in letters)