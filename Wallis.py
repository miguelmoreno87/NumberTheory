"""
Wallis Module

It contains functions concerning the Wallis product
"""


def producto(n):
    p = 1
    for i in range(1, n):
        p *= ((2*i)**2)/((2*i-1)*(2*i+1))

    return p
