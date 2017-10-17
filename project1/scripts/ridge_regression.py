# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lambda_):
    """implement ridge regression."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # ridge regression: TODO
    # ***************************************************
    x_tr = tx.transpose()
    lambda_prime = lambda_ * 2 * y.shape[0]
    op1 = (x_tr @ tx)
    op2 = (lambda_prime * np.eye(tx.shape[1]))
    X = (x_tr @ tx) + (lambda_prime * np.eye(tx.shape[1]))
    Y = x_tr @ y
    w_ridge = (np.linalg.solve(X, Y))      
    return w_ridge