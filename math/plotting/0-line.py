#!/usr/bin/env python3
'''
Plotting x and y with a redline, and limitting x to range 10
'''

import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3
x = np.arange(0, 11)

plt.plot(x, y, "r-")
plt.xlim(0, 10)
plt.show()
