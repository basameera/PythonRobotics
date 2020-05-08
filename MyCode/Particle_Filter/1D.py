import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    velocity = 1  # m/s
    DT = 0.1  # sec
    start_pos = 0  # meters
    time = 0.0

    SIM_TIME = 10

    positions = []
    pos = start_pos
    positions.append(pos)

    # for t in range(sim_time):
    #     pos = pos + (velocity * DT)
    #     positions.append(pos)

    show_animation = True

    while SIM_TIME >= time:
        time += DT

        pos += velocity * DT
        # print(pos)

        if show_animation:
            plt.cla()
            # for stopping simulation with the esc key.
            plt.gcf().canvas.mpl_connect('key_release_event',
                                         lambda event: [exit(0) if event.key == 'escape' else None])
            plt.scatter(pos, 0)
            plt.grid(True)
            plt.xlim(-1, 11)
            plt.xlabel('X Position (m)')
            plt.title('Simulation time: {:.2f} seconds'.format(time))

            plt.pause(0.001)
