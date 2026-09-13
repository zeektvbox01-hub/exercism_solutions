def label(colours):
    total_sum = 0
    total_sum += colour_code(colours[0]) * 10
    total_sum += colour_code(colours[1])
    total_sum *= colour_code_powers(colours[2])
    total_sum = int(total_sum)
    if int(total_sum//1e9) >= 1:
        return str(int(total_sum//1e9)) + " gigaohms"
    if int(total_sum//1e6) >= 1:
        return str(int(total_sum//1e6)) + " megaohms"
    if int(total_sum//1000) >= 1:
        return str(int(total_sum//1000)) + " kiloohms"
    return str(total_sum) + " ohms"
    
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

def colour_code_powers(colour):
    return {
    "black": 1,
    "brown": 10,
    "red": 100,
    "orange": 1000,
    "yellow": 1e4,
    "green": 1e5,
    "blue": 1e6,
    "violet": 1e7,
    "grey": 1e8,
    "white": 1e9,
    }.get(colour)

