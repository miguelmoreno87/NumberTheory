"""
Módulo Wallis

Contiene funciones relacionadas con el producto de Wallis
"""


def producto(N):
    p = 1
    for n in range(1, N):
        p *= ((2*n)**2)/((2*n-1)*(2*n+1))

    return p
