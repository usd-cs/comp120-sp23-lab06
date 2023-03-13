"""
Module: comp120_lab06

Starter code for COMP120 Lab 06
"""
from sys import argv

def is_measurable(target: int, weights: list[int]) -> bool:
    """Determines whether we could accurately measure an object of the
    <target> size, given weights of the given sizes and a two-pan balance.

    Parameters:
        target (int): The weight of the object to measure
        weights (list[int]): List of the sizes of weights available to use
            during measuring.

    Returns:
        (bool) True if the target weight can be measured using the given list
        of weights, False otherwise.

    >>> is_measurable(2, [1,3])
    True
    >>> is_measurable(5, [1,3])
    False
    >>> is_measurable(6, [1,3,7])
    True
    """

    return False  # dummy implementation...



# Application Code

if __name__ == "__main__":
    if len(argv) >= 2:
        target_weight = int(argv[1])
        weights = [int(n) for n in argv[2:]]

        if is_measurable(target_weight, weights):
            print("The target item can be measured!")
        else:
            print("The target item CANNOT be measured!")

    else:
        print("Incorrect number of parameters. Need a target and (optional) weights")
