def commands(binary_str):
    actions = []
    binary_str = " ".join(binary_str)
    binary_code = binary_str.split()
    if binary_code[-1] == "1":
        actions.append("wink")
    if binary_code[-2] == "1":
        actions.append("double blink")
    if binary_code[-3] == "1":
        actions.append("close your eyes")
    if binary_code[-4] == "1":
        actions.append("jump")    
    if binary_code[-5] == "1":
        actions.reverse()
    return actions