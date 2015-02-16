import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

alpha, beta = 0.4, 0.5
def f(x1, x2):
    return alpha * np.log(x1) + beta * np.log(x2)

p1, p2, m = 1.0, 1.2, 4
def budget_line(x1):
    return (m - p1 * x1) / p2

x1star = (alpha / (alpha + beta)) * (m / p1)
x2star = budget_line(x1star)
maxval = f(x1star, x2star)

xgrid = np.linspace(1e-2, 4, 50)
ygrid = xgrid

# === plot value function === #
fig, ax = plt.subplots(figsize=(8,6))
x, y = np.meshgrid(xgrid, ygrid)

if 1:
    ax.plot(xgrid, budget_line(xgrid), 'k-', lw=2, alpha=0.8)
    #ax.fill_between(xgrid, xgrid * 0.0, budget_line(xgrid), facecolor='blue', alpha=0.3)

if 0:  # Annotate with text
    ax.text(1, 1, r'$p_1 x_1 + p_2 x_2 < m$', fontsize=16)

    ax.annotate(r'$p_1 x_1 + p_2 x_2 = m$', 
             xy=(2, budget_line(2)),  
             xycoords='data',
             xytext=(40, 40),
             textcoords='offset points',
             fontsize=16,
             arrowprops=dict(arrowstyle="->"))

if 1:  # Add maximizer
    ax.annotate(r'$(x_1^*, x_2^*)$', 
             xy=(x1star, x2star),  
             xycoords='data',
             xytext=(30, 30),
             textcoords='offset points',
             fontsize=16,
             arrowprops=dict(arrowstyle="->"))
    ax.plot([x1star], [x2star],  'ro', alpha=0.6)


if 1:  # Plot with contours
    #points = [-10, -2, -1, 0, 0.4, 0.6, 0.8, 1.0, 1.2, 4]
    points = [-10, -2, -1, 0, 0.6, 1.0, 1.2, 4]
    ax.contourf(x, y, f(x, y), points, cmap=cm.jet, alpha=0.5)
    cs = ax.contour(x, y, f(x, y), points, colors='k', linewidth=2, alpha=0.7,
            antialias=True)
    plt.clabel(cs, inline=1, fontsize=12)

ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.set_xticks((0.0, 1.0, 2.0, 3.0))
ax.set_yticks((1.0, 2.0, 3.0))
ax.set_xlabel(r'$x_1$', fontsize=16)
ax.set_ylabel(r'$x_2$', fontsize=16)
plt.show()


