#!/usr/bin/python3
"""Say my name"""


def print_square(size):
    """Prints My name is <first_name> <last_name>

    Args:
        size (int): size of the square

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for k in range(size):
        print("#" * size)
