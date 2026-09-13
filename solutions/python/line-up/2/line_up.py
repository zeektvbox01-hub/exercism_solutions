def line_up(name, number):
    ordinal_number = ""
    if number % 100 in {11,12,13}:
        ordinal_number = str(number) + "th"
    elif number % 10 == 1:
        ordinal_number = str(number) + "st"
    elif number % 10 == 2:
        ordinal_number = str(number) + "nd"
    elif number % 10 == 3:
        ordinal_number = str(number) + "rd"
    else:
        ordinal_number = str(number) + "th"
    return name + ", you are the " + ordinal_number + " customer we serve today. Thank you!"