""" Here is the source code of the tool you can use to make your very own Guido's Gorgeous Lasagna"""
EXPECTED_BAKE_TIME = 40
LAYER_PREP_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """  Calculates the remaining bake time
    
    Parameters:
        elapsed_bake_time (int): How long the lasagna has been baking

    Constants:
        EXPECTED_BAKE_TIME (int): The expected time the lasagna will take to bake
    
    Returns:
        int: How long it will take to prepare all the layers

    Examples:
        >>> bake_time_remaining(15):
        25
        >>> bake_time_remaining(23):
        17
        
    Subtracts the elapsed bake time from the expected total bake time and returns the difference
    """
    
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """  Calculates the additional preparation time
    
    Parameters:
        number_of_layers (int): The number of layers to prepare

    Constants:
        LAYER_PREP_TIME (int): The time it takes for a layer to be prepared
    
    Returns:
        int: How long it will take to prepare all layers
        
    Examples:
        >>> preparation_time_in_minutes(4):
        8
        >>> preparation_time_in_minutes(13)):
        26
    
    Multiplies the numper of layers by the layer's preparation time,and returns the product
    """
    
    return number_of_layers * LAYER_PREP_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ Calculates the total elapsed time
    
    Parameters:
        elapsed_bake_time (int): How long the lasagna has been baking
        number_of_layers (int): The number of layers to prepare
    
    Returns:
        int: The total elasped time
        
    Examples:
        >>> elapsed_time_in_minutes(15, 4):
        23
        >>> elapsed_time_in_minutes(23, 13):
        49
        
    Adds the elapsed bake time to the numper of layers multiplied by the layer's preparation time and returns the sum
    """

    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)