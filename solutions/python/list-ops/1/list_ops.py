def append(list1, list2):
    for term in list2:
        list1.append(term)
    return list1

def concat(lists):
    final_list = []
    for item in lists:
        if item is None:
            continue
        if isinstance(item, list):
            final_list.extend(item)
        else:
            final_list.append(item)
    return final_list


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return len(list)

def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, list, initial):
    accumulator = initial
    list.reverse()
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def reverse(list):
    list.reverse()
    return list