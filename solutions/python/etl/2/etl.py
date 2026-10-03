def transform(legacy_data):
    data = {}
    for key in legacy_data:
        for letter in legacy_data[key]:
            lower_letter = letter.lower()
            data[lower_letter] = key
    return data
        
