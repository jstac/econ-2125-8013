import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

alpha, beta = 0.4, 0.5
def f(x, y):
    return x**alpha * y**beta

xgrid = np.linspace(0, 3, 50)
ygrid = xgrid

# === plot value function === #
fig, ax = plt.subplots(figsize=(8,6))
x, y = np.meshgrid(xgrid, ygrid)
ax.contourf(x, y, f(x, y), 10, cmap=cm.jet, alpha=0.5)
cs = ax.contour(x, y, f(x, y), 10, colors='k', linewidth=2, alpha=0.8)
plt.clabel(cs, inline=1, fontsize=12)
ax.set_xticks((0.0, 1.0, 2.0, 3.0))
ax.set_yticks((1.0, 2.0, 3.0))
ax.set_xlabel(r'$k$', fontsize=16)
ax.set_ylabel(r'$\ell$', fontsize=16)
plt.show()


