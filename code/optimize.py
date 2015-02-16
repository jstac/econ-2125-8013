"""
Minimize the function

        f(x) := - \exp
        \left\{-\frac{(x - 5.0)^4}{1.5} \right\}
"""

from scipy.optimize import fminbound
import numpy as np
def f(x): return -np.exp(-(x - 5.0)**4 / 1.5)
print fminbound(f, -10, 10)  # Find approx solution
