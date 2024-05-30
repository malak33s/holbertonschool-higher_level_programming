#!/usr/bin/python3
"""Define the triangle pascal"""


def pascal_triangle(n):
    """Define function pascal_triangle

    Args:
        n (int): num of row
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for cpt in range(1, n):
        line = [1]
        for cpt_it in range(1, cpt):
            line.append(triangle[cpt-1][cpt_it-1] + triangle[cpt-1][cpt_it])
        line.append(1)
        triangle.append(line)
    return triangle
