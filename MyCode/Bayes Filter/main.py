import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Chebyshev as T
from utils import *
from skylynx.utils import cli_args

if __name__ == "__main__":
    # argparse
    cli_params = dict(
        DT=5,
    )

    args = cli_args(cli_params)

    velocity = 1  # m/s
    DT = int(args['DT'])  # sec
    start_pos = 0  # meters
    time = 0.0

    plane_height = 10

    pos = start_pos

    x = np.linspace(-1, 0.9, 100)
    y1 = T.basis(2)(x) + T.basis(5)(x)
    y2 = T.basis(3)(x) + T.basis(5)(x)
    y3 = T.basis(4)(x) + T.basis(5)(x)

    ly = np.concatenate((y2, y1, y3))
    ly_min = abs(np.min(ly))
    ly = ly + (ly_min*2)

    lx = np.arange(len(ly))

    # std
    std = 1
    # y_sine_noise = create_toy_data(ly, std)

    SIM_TIME = len(ly)

    show_animation = True

    fig, axs = plt.subplots(1, 1, figsize=(14, 5))
    ax = axs
    ax.set_axisbelow(True)

    # while SIM_TIME > time:
    for pos in range(0, len(lx), DT):

        if show_animation:
            plt.cla()
            # for stopping simulation with the esc key.
            plt.gcf().canvas.mpl_connect('key_release_event',
                                         lambda event: [exit(0) if event.key == 'escape' else None])

            ax.grid(ls='--')
            ax.plot(lx, ly, c='g')
            ax.fill_between(lx, ly, color="green", alpha=0.6)

            # std range
            ax.fill_between(lx, ly - std, ly + std,
                            color="gray", label="std.", alpha=0.5)

            # Plot plane route
            ax.axhline(y=plane_height, xmin=0, xmax=1,
                       c='r', ls='--', lw=1)
            # plane current pos
            ax.scatter(pos, plane_height, c='r', lw=3, marker='>')

            # distance to current height
            ax.scatter(pos, ly[pos], c='k', lw=2)

            # noise within std
            # ax.scatter(lx, y_sine_noise, c='b', marker='*', lw=0.5, alpha=0.5)

            # current noisy distance sample
            # ax.scatter(pos, y_sine_noise[pos], c='k', marker='*', lw=0.5)

            # settings
            ax.grid(True)
            # plt.xlim(-1, SIM_TIME)
            ax.set_xlabel('X Position (m)')
            ax.set_ylabel('Height (m)')
            ax.set_title('Simulation time: {:.1f} seconds'.format(pos+DT))

            plt.pause(0.001)

    if show_animation:
        plt.show()
