import enum


class Operations(enum.Enum):
    Union = 0
    Intersection = 1
    Equivalence = 2
    Modulo2Sum = 3
    Implication = 4
    SchaefferStroke = 5
    PierceArrow = 6


def execute(operation: Operations, a: bool, b: bool) -> bool:
    if operation == Operations.Union:
        return a is True or b is True
    elif operation == Operations.Intersection:
        return a is True and b is True
    elif operation == Operations.Equivalence:
        return a == b
    elif operation == Operations.Modulo2Sum:
        return a != b
    elif operation == Operations.Implication:
        return a is not True or b is not False
    elif operation == Operations.SchaefferStroke:
        return a is False or b is False
    elif operation == Operations.PierceArrow:
        return a is False and b is False

    return False
