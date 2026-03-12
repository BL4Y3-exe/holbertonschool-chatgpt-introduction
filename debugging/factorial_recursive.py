#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    ---------------------
    Recursively calculates the factorial of a non-negative integer n.
    The factorial of n (denoted n!) is the product of all positive integers from 1 to n.
    For example, 5! = 5 × 4 × 3 × 2 × 1 = 120.

    Parameters:
    -----------
    n : int
        A non-negative integer whose factorial is to be calculated.

    Returns:
    --------
    int
        The factorial of the input number n.
        Returns 1 if n is 0 (by definition, 0! = 1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the first command-line argument and convert it to an integer
f = factorial(int(sys.argv[1]))

# Print the factorial result
print(f)