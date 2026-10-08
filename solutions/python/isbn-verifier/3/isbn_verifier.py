def is_valid(isbn):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    isbn = ' '.join(isbn)
    isbn = isbn.split()
    count = 0
    for index,key in enumerate(isbn):
        if key == '-':
            del isbn[index]
            if isbn[index] == 'X':
                if not isbn[-1]:
                    return False
                isbn[-1] = '10'
            elif isbn[index] not in numbers:
                return False
        elif key == 'X':
            if not isbn[-1]:
                return False
            isbn[-1] = '10'
        elif key not in numbers:
            return False
        count += 1
    if count != 10:
        return False
    for index,key in enumerate(isbn):
        isbn[index]= int(key)
    formula_result = (isbn[0] * 10 + isbn[1] * 9 + isbn[2] * 8 + isbn[3] * 7 + isbn[4] * 6 + isbn[5] * 5 + isbn[6] * 4 + isbn[7] * 3 + isbn[8] * 2 + isbn[9]) % 11
    return formula_result == 0
