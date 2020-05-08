import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Chebyshev as T

if __name__ == "__main__":

    x = np.linspace(-1, 0.9, 100)

    y1 = T.basis(2)(x) + T.basis(5)(x)
    y2 = T.basis(3)(x) + T.basis(5)(x)
    y3 = T.basis(4)(x) + T.basis(5)(x)

    # Poly curves
    # fig, axs = plt.subplots(1, 1, figsize=(6, 4))

    # ax = axs
    # ax.set_axisbelow(True)
    # ax.grid(ls='--')

    # ax.plot(x, y1, label='y1')
    # ax.plot(x, y2, label='y2')
    # ax.plot(x, y3, label='y3')

    # ax.legend(loc="upper left")

    # Mountains
    fig, axs = plt.subplots(1, 1, figsize=(14, 5))
    ax = axs
    ax.set_axisbelow(True)
    ax.grid(ls='--')

    ly = np.concatenate((y2, y1, y3))
    ly = ly + abs(np.min(ly))
    lx = np.arange(len(ly))

    # plot mountain
    ax.plot(lx, ly, c='g')
    ax.fill_between(lx, ly, color="green", alpha=0.6)

    # Plot plane route
    ax.axhline(y=5, xmin=0, xmax=1, c='r', ls='--', lw=0.75)

    ax.set_xlabel('X position (m)')
    ax.set_ylabel('Height (m)')

    plt.show()
