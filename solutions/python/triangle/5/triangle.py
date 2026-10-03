def equilateral(sides:list) -> bool:
    """ Verify that the triangle is equilateral based on its sides
 
    Parameters:
        sides: The values of the three sides
 
    Returns:
        Is it an equilateral triangle?
 
    """
    return triangle_check(sides,[1])

def isosceles(sides:list) -> bool:
    """ Verify that the triangle is isosceles based on its sides
 
    Parameters:
        sides: The values of the three sides
 
    Returns:
        Is it an isosceles triangle?
 
    """
    return triangle_check(sides,[1,2])

def scalene(sides:list) -> bool:
    """ Verify that the triangle is scalene based on its sides
 
    Parameters:
        sides: The values of the three sides
 
    Returns:
        Is it a scalene triangle?
 
    """
    return triangle_check(sides,[3])

def triangle_check(sides: list, requirement: list) -> bool:
    """ Verify that the triangle is of a certain type based on its sides
 
    Parameters:
        sides: The values of the three sides
        requirement: The needed side lengths to be defined as a certain type
 
    Returns:
        Is it a triangle of a certain type?
 
    """
    return sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[2] + sides[0] > sides[1] and len(set(sides)) in requirement