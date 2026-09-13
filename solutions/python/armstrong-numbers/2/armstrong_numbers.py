def is_armstrong_number(number):
    digits = [int(string_digits) for string_digits in str(number)]
    digit_count = len(str(number))
    total_sum = 0
    for string_digits in digits:
        total_sum += string_digits ** digit_count
    return total_sum == number