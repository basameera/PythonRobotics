import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Chebyshev as T

if __name__ == "__main__":
    velocity = 1  # m/s
    DT = 1  # sec
    start_pos = 0  # meters
    time = 0.0

    plane_height = 5

    pos = start_pos

    x = np.linspace(-1, 0.9, 100)
    y1 = T.basis(2)(x) + T.basis(5)(x)
    y2 = T.basis(3)(x) + T.basis(5)(x)
    y3 = T.basis(4)(x) + T.basis(5)(x)

    ly = np.concatenate((y2, y1, y3))
    ly = ly + abs(np.min(ly))
    lx = np.arange(len(ly))

    SIM_TIME = len(ly)

    show_animation = True

    fig, axs = plt.subplots(1, 1, figsize=(14, 5))
    axs.set_axisbelow(True)

    while SIM_TIME >= time:
        time += DT
        print(time, ly[int(time)], end='\r')
        pos += velocity * DT

        if show_animation:
            plt.cla()
            # for stopping simulation with the esc key.
            plt.gcf().canvas.mpl_connect('key_release_event',
                                         lambda event: [exit(0) if event.key == 'escape' else None])

            axs.grid(ls='--')
            axs.plot(lx, ly, c='g')
            axs.fill_between(lx, ly, color="green", alpha=0.6)

            # Plot plane route
            axs.axhline(y=plane_height, xmin=0, xmax=1,
                        c='r', ls='--', lw=1)
            # plane current pos
            axs.scatter(pos, plane_height, c='r', lw=3)

            # distance to current height
            axs.scatter(pos, ly[int(time)], c='k', lw=3)

            # settings
            axs.grid(True)
            # plt.xlim(-1, SIM_TIME)
            axs.set_xlabel('X Position (m)')
            axs.set_ylabel('Height (m)')
            axs.set_title('Simulation time: {:.2f} seconds'.format(time))

            plt.pause(0.001)
