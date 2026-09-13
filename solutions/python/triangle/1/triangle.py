def equilateral(sides):
    if (
        sides[0] + sides[1] <= sides[2]
        or sides[1] + sides[2] <= sides[0]
        or sides[2] + sides[0] <= sides[1]
    ):
        return False
    unique_count = len(set(sides))
    if unique_count == 1:
        return True
    return False

def isosceles(sides):
    if (
        sides[0] + sides[1] < sides[2]
        or sides[1] + sides[2] < sides[0]
        or sides[2] + sides[0] < sides[1]
    ):
        return False
    unique_count = len(set(sides))
    if unique_count == 2 or unique_count == 1:
        return True
    return False


def scalene(sides):
    if (
        sides[0] + sides[1] < sides[2]
        or sides[1] + sides[2] < sides[0]
        or sides[2] + sides[0] < sides[1]
    ):
        return False
    unique_count = len(set(sides))
    if unique_count == 3:
        return True
    return False
