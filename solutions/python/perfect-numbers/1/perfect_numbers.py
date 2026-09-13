"Find whether a number is perfect, abundant, or deficient?"

def classify(number):
    if number % 1 != 0 or number <= 0 :
        raise ValueError("Classification is only possible for positive integers.")
    if number == { 6, 28, 496, 8128, 33550336, 8589869056,137438691328}:
        return "perfect"
    factors = [factor for factor in range(1, number) if number % factor == 0]
    total_sum = 0
    for factor in factors:
        total_sum += factor
    if total_sum == number:
        return "perfect"
    if total_sum > number:
        return "abundant"
    return "deficient"
    
