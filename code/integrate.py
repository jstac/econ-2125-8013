"""
Integrate the function

    \frac{1}{\sqrt{2\pi}} 
        \int_{-2}^2 
        \exp\left\{ - \frac{x^2}{2} \right\} dx
"""

from scipy.stats import norm
from scipy.integrate import quad
phi = norm()
value, error = quad(phi.pdf, -2, 2)
print value

