

# -*- coding: utf-8 -*-
# Useful starting lines

import numpy as np

"""Functions used to compute the loss."""

def compute_loss_mse(y, tx, w):
    e = y - np.sum(tx*w, axis = 1)
    n = y.shape[0]
    scalaire = (1.0/(2.0*n))
    cost_matrix = (1.0/(2.0*n)) * (e * e)
    
    return np.sum(cost_matrix)


def compute_loss_mae(y, tx, w):
    e = y - np.sum(tx*w, axis = 1)
    n = y.shape[0]
    scalaire = (1.0/(2.0*n))
    cost_matrix = (1.0/(2.0*n)) * (np.absolute(e))
    
    return np.sum(cost_matrix)
    
def compute_loss_rmse(y, tx, w):
    return np.sqrt(2 * compute_loss_mse(y, tx, w))