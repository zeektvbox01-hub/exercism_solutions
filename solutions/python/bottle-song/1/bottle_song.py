WORD_NUMBERS = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

def recite(start, take=1):
    final_list = []
    for number in range(1,(take + 1)):
        if (start + 1) - number == 1:
            final_list.append("One green bottle hanging on the wall,")
            final_list.append("One green bottle hanging on the wall,")
        else:
            final_list.append(WORD_NUMBERS[(start + 1) - number].capitalize() + " green bottles hanging on the wall,")
            final_list.append(WORD_NUMBERS[(start + 1) - number].capitalize() + " green bottles hanging on the wall,")
        final_list.append("And if one green bottle should accidentally fall,")
        if start - number == 1:
            final_list.append("There'll be one green bottle hanging on the wall.")
        else:
            final_list.append("There'll be " + WORD_NUMBERS[start - number] + " green bottles hanging on the wall.")
        if number != take:
            final_list.append("")
    return final_list
