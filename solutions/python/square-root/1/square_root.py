def square_root(number):
    square_root_testing = 1
    while square_root_testing * square_root_testing != number:
        square_root_testing += 1
    return square_root_testing 
