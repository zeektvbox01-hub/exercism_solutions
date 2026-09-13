EXPECTED_BAKE_TIME = 40
bake_time_left = 40
additional_time = 2

def bake_time_remaining(elapsed_bake_time):
    """Why do I need to do this"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Why do I need to do this"""
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Why do I need to do this"""
    bake_time_left = bake_time_remaining(elapsed_bake_time)
    additional_time = preparation_time_in_minutes(number_of_layers)
    return 40 - bake_time_left + additional_time