# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


from costs import *
def least_squares(y, tx):
    """calculate the least squares solution."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    Xtr = np.transpose(tx)
    X = Xtr@tx
    Y = Xtr@y
    w_opt = np.linalg.solve(X, Y)

    mse = compute_loss_mse(y, tx, w_opt)
    
    return mse, w_opt
    # least squares: TODO
    # returns mse, and optimal weights
    # ***************************************************