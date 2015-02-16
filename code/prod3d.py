import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
from matplotlib import cm

alpha, beta = 0.4, 0.5
def f(x, y):
    return x**alpha * y**beta

xgrid = np.linspace(0, 3, 50)
ygrid = xgrid

# === plot value function === #
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
x, y = np.meshgrid(xgrid, ygrid)
ax.plot_surface(x,
                y,
                f(x, y),
                rstride=5, cstride=5,
                cmap=cm.jet,
                alpha=0.4,
                linewidth=0.25)
#ax.set_zlim(-0.5, 1.0)
ax.set_xticks((0.0, 1.0, 2.0, 3.0))
ax.set_zticks((0.0, 1.0, 2.0, 3.0))
ax.set_yticks((1.0, 2.0, 3.0))
ax.set_xlabel(r'$k$', fontsize=16)
ax.set_ylabel(r'$\ell$', fontsize=16)
ax.set_zlabel(r'$f(k, \ell)$', fontsize=16)
plt.show()
