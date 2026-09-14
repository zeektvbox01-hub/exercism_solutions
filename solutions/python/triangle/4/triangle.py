def equilateral(sides:list) -> bool:
    return triangle_check(sides,[1])

def isosceles(sides:list) -> bool:
    return triangle_check(sides,[1,2])

def scalene(sides:list) -> bool:
    return triangle_check(sides,[3])

def triangle_check(sides:list,requirement:list) -> bool:
    unique_count:int = len(set(sides))
    return sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[2] + sides[0] > sides[1] and unique_count in requirement