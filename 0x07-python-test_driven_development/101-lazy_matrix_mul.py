#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy.
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
        or contains non-integer/float values.
        ValueError: If m_a or m_b is empty, not a rectangle, or cannot be multiplied.

    Returns:
        list of lists of ints/floats: The product of m_a and m_b.

    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_a = np.array(m_a)
    m_b = np.array(m_b)

    return (np.dot(m_a, m_b).tolist())
