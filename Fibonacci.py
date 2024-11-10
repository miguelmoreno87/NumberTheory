"""
Módulo Fibonacci

Contiene funciones relacionadas con la sucesión de Fibonacci
"""

def fib1(n):
    """
    Muestra los números de la sucesión de Fibonacci inferiores al valor introducido
    """
    a, b = 0, 1

    while a < n:
        print(a, end=" ")
        aux = b
        b = a+b
        a = aux

    print()


def fib2(n):
    """
    Calcula el número aúreo utilizando los números de la sucesión de Fibonacci
    """
    a, b = 0, 1

    while a < n:
        aux = b
        b = a+b
        a = aux

    print(1+(a/b))
