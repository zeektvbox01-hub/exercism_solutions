def value(colours):
    total_sum = 0
    total_sum += colour_code(colours[0]) * 10
    total_sum += colour_code(colours[1])
    return total_sum
        
def colour_code(colour):
    return {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
    }.get(colour)
