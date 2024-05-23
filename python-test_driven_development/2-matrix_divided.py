#!/usr/bin/python3
"""Define a division function and a matrix"""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix

    matrix must be a list of lists of integers or floats

    Raises:

    ZeroDivisionError: if division by zero
    TypeError: if div must be a number
    TypeError: if matrix must be a matrix (list of lists) of integers/float
    TypeError: if Each row of the matrix must have the same size
    """
    # verif if the matrix is a list of lists of int and floats
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(ele / div, 2) for ele in row] for row in matrix]
