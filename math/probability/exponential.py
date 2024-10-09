#!/usr/bin/env python3
"""Create a class Exponential that represents an
exponential distribution"""


class Exponential:
    """class Exponential"""

    def __init__(self, data=None, lambtha=1.):
        """Constructor"""

        self.E = 2.7182818285
        self.PI = 3.1415926536

        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            else:
                self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = 1/(float(sum(data) / len(data)))