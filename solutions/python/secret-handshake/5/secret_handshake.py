ACTION_LIST = ["wink", "double blink", "close your eyes", "jump"]

def commands(binary_str):
    
    actions = []
    for index, value in enumerate(reversed(binary_str[1:6])):
        if value == "1":
            actions.append(ACTION_LIST[index])
    if binary_str[0] == "1":
        actions.reverse()
    return actions