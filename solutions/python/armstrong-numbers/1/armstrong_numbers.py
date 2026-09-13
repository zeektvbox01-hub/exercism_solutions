def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]
    digit_count = len(str(number))
    total_sum = 0
    for d in digits:
        total_sum += d ** digit_count
    return total_sum == number