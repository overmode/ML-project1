# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    
    xs = np.tile(x, (degree + 1, 1)).transpose()
    powers = np.arange(degree + 1)
    return np.power(xs, powers)
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    # ***************************************************
