"""
Fibonacci Module

It contains functions concerning the Fibonacci sequence
"""
import numpy as np


def sequence(n):
    """
    It shows every number inferior to the input number of the Fibonacci sequence
    """
    a, b = 0, 1

    while a < n:
        print(a, end=" ")
        aux = b
        b = a+b
        a = aux

    print()


def golden_ratio(n):
    """
    It calculates the golden ratio using the Fibonacci sequence
    """
    a, b = 0, 1

    while a < n:
        aux = b
        b = a+b
        a = aux

    print(1+(a/b))


def combinatorial_number(n, k):
    """
    Function that calculates the combinatorial number (n,k) using Pascal's triangle
    """
    pascal = np.zeros((n+1, n+1), dtype=int)
    pascal[0][0] = 1

    for i in range(1, n+1):
        for j in range(i+1):
            if j == 0:
                pascal[i][j] = 1
            elif j == i:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    if k <= n:
        return pascal[n][k]
    else:
        return "Error"
