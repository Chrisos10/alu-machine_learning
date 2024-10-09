#!/usr/bin/env python3
"""Create a class Binomial that represents a binomial distribution
"""


class Binomial:
    """Class Binomial"""

    def __init__(self, data=None, n=1, p=0.5):
        """Constructor"""

        if data is None:
            if n <= 0:
                raise ValueError('n must be a positive value')
            if p <= 0 or p >= 1:
                raise ValueError('p must be greater than 0 and less than 1')
            self.n = int(n)
            self.p = float(p)

        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            mean = float(sum(data) / len(data))
            var = float((sum(map(lambda n: pow(n - mean,
                        2), data)) / len(data)))
            self.p = 1 - (var / mean)
            self.n = round(mean / self.p)
            self.p = mean / self.n
