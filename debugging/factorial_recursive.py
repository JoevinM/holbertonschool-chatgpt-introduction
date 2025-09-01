#!/usr/bin/python3
"""
Script that calculates the factorial of a number passed as an argument.
Usage: ./factorial.py <number>
"""
import sys

def factorial(n):
     """
    Computes the factorial of an integer n recursively.
    Returns 1 if n is 0, otherwise returns n * factorial(n-1).

    Args:
        n (int): The integer to compute the factorial of.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)