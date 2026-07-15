"""Functions to determine if a triangle is equilateral, isosceles or scalene."""


def is_valid_triangle(sides):
    """Check if the given sides form a valid triangle."""
    if len(sides) != 3:
        return False
    side_one, side_two, side_three = sides
    if side_one <= 0 or side_two <= 0 or side_three <= 0:
        return False
    return (side_one + side_two >= side_three and
            side_one + side_three >= side_two and
            side_two + side_three >= side_one)


def equilateral(sides):
    """Determine if a triangle is equilateral."""
    if not is_valid_triangle(sides):
        return False
    return len(set(sides)) == 1


def isosceles(sides):
    """Determine if a triangle is isosceles."""
    if not is_valid_triangle(sides):
        return False
    return len(set(sides)) <= 2


def scalene(sides):
    """Determine if a triangle is scalene."""
    if not is_valid_triangle(sides):
        return False
    return len(set(sides)) == 3