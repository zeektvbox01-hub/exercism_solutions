""" Tools to help you make Guido's Gorgeous Lasagna

Constants:
    EXPECTED_BAKE_TIME: The expected time the lasagna will take to bake
    LAYER_PREP_TIME (int): The time it takes for a layer to be prepared

"""

EXPECTED_BAKE_TIME: int = 40
LAYER_PREP_TIME: int = 2

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """  Calculates the remaining bake time
    
    Parameters:
        elapsed_bake_time: How long the lasagna has been baking
    
    Returns:
        How long it will take to prepare all the layers
    """
    
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers: int) -> int :
    """  Calculates the additional preparation time
    
    Parameters:
        number_of_layers: The number of layers to prepare
    
    Returns:
        How long it will take to prepare all layers
    """
    
    return number_of_layers * LAYER_PREP_TIME

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """ Calculates the total elapsed time
    
    Parameters:
        elapsed_bake_time: How long the lasagna has been baking
        number_of_layers: The number of layers to prepare
    
    Returns:
        The total elapsed time
    """

    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)