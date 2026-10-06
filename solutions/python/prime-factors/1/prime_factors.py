def factors(value):
    new_value = value
    prime_factors = []
    testing_number = 2
    while new_value != 1:
        if new_value % testing_number == 0:
            prime_factors.append(testing_number)
            new_value = new_value // testing_number
        else:
            testing_number += 1
    return prime_factors
        
