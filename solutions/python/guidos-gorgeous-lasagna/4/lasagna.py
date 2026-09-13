""" Here is the source code of the tool you can use to make your very own Guido's Gorgeous Lasagna"""
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """ Why do I need to do this?"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """ Why do I need to do this?"""
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ Why do I need to do this?"""
    remaining_wait_time = bake_time_remaining(elapsed_bake_time)
    new_time_added = preparation_time_in_minutes(number_of_layers)
    return 40 - remaining_wait_time + new_time_added