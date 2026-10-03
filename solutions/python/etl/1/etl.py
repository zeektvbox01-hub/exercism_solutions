def transform(legacy_data):
    data = {}
    for key in legacy_data:
        list_for_scores = []
        for letter in legacy_data[key]:
            letter = letter.lower()
            data[letter] = key
    return data
        
