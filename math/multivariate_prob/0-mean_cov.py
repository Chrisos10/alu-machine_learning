#!/usr/bin/env python3
"""
    a function def mean_cov(X):
    that calculates the mean and covariance of a data set:
"""


import numpy as np


def mean_cov(X):
    """

    A function that returns:
        mean is a numpy.ndarray of shape (d,) containing the mean
        of the data set
        cov is a numpy.ndarray of shape (d, d) containing the
        covariance matrix of the data set
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    if X.shape[0] < 2:
        raise ValueError("X must contain multiple data points")

    n, d = X.shape
    mean = np.mean(X, axis=0, keepdims=True)
    centered_data = X - mean
    cov = np.dot(centered_data.T, centered_data) / (n - 1)
    return mean, cov
