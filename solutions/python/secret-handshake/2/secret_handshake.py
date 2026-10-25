def commands(binary_str):
    action_list = ["jump","close your eyes","double blink","wink"]
    actions = []
    for index in reversed(range(1,5)):
        if binary_str[index] == "1":
            actions.append(action_list[(index - 1)])
    if binary_str[0] == "1":
            actions.reverse()
    return actions