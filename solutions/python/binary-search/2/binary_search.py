def find(search_list, value):
    try: 
        return search_list.index(value) 
    except ValueError as error :
        raise ValueError("value not in array") from error
