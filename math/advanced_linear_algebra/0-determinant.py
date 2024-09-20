#!/usr/bin/env python3
"""
Module to calculate the determinant of a matrix.
"""


def determinant(matrix):
    """
    Calculate the determinant of a matrix. Validates that the input is a
    list of lists and checks for squareness. Handles 0x0 matrices by
    returning 1, in accordance with mathematical conventions.
    """
    # Validate matrix format
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    num_rows = len(matrix)

    # Early return for 0x0 matrix
    # Check if the matrix is empty
    if matrix == [[]]:  # Handle empty matrix [[]] as a special case
        return 1

    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")

    # Handle 1x1 matrix case
    if len(matrix) == 1:
        return matrix[0][0]

    # Handle 2x2 matrix case
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case for matrices larger than 1x1
    det = 0
    for col in range(num_rows):
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        cofactor = (-1) ** col * matrix[0][col] * determinant(minor)
        det += cofactor

    return det
