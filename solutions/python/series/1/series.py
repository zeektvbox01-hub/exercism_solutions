def slices(series, length):
    if not series:
        raise ValueError("series cannot be empty")
    number_str = series.lower() 
    number_str = "_".join(number_str) 
    number_list = number_str.split("_")
    series_length = len(number_list)
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0: 
        raise ValueError("slice length cannot be negative")
    if length > series_length:
        raise ValueError("slice length cannot be greater than series length")
    list_of_sets = []
    for index in range(series_length - length + 1):
        new_number = ""
        for offset in range(length):
            new_number += number_list[index + offset]
        list_of_sets.append(new_number)
    return list_of_sets
    