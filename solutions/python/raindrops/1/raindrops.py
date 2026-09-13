def convert(number):
    final_string = ""
    if number % 3 == 0:
        final_string = final_string + "Pling"
    if number % 5 == 0:
        final_string = final_string + "Plang"
    if number % 7 == 0:
        final_string = final_string + "Plong"
    if final_string == "":
        final_string = str(number)
    return final_string
