from skylynx.utils import cli_args
from utils import *
import matplotlib.pyplot as plt
import numpy as np


def ax_set_settings(ax):
    ax.set_axisbelow(True)
    ax.grid(ls='--')
    ax.set_xlabel('')
    ax.set_xlim(-1, 11)
    ax.set_ylim(0, 1)
    ax.set_title('Bayes Filter')
    ax.legend()


click_counter = 0


def get_color_label():
    global click_counter
    if click_counter % 2 == 0:
        color = 'tab:blue'
        label = 'Mesurement'
    else:
        color = 'tab:orange'
        label = 'Motion'
    return color, label


def task_3():

    def onclick(event):
        # print('you pressed', event.key, event.xdata, event.ydata)
        global click_counter
        if event.key == 'escape':
            exit(0)
        elif event.key == 'right':
            ax.clear()
            data = np.random.random((10,))
            c, l = get_color_label()
            ax.scatter(data, data, c=c, label=l)
            ax_set_settings(ax)

            fig.canvas.draw()
            click_counter += 1

    fig, axs = plt.subplots(1, 1, figsize=(14, 5))
    ax = axs

    cid = fig.canvas.mpl_connect('key_release_event', onclick)
    ax.plot(np.arange(0, 1, 0.1), c='tab:blue', label='Init')
    ax_set_settings(ax)
    plt.show()


def task_2():
    """Main window
    """

    fig, axs = plt.subplots(1, 1, figsize=(8, 4))

    simulation_scope = 10

    # Initial p(x)
    p = [0.5, 0.5]
    y = np.array(p)

    y = np.concatenate((y, np.zeros(simulation_scope-len(p),)))

    x = np.arange(simulation_scope)

    ax = axs
    ax.set_title(r'Initial $p(x)$')
    bar_plot(ax, x, y, color='k')

    ax.set_xlim(-1, simulation_scope+1)

    plt.show()


def task_1():
    """PDF as bar plot
    """

    fig, axs = plt.subplots(1, 2, figsize=(8, 4))

    # Mesurement model
    y = np.ones(shape=(3,))/3
    x = np.arange(len(y)) - 1

    ax = axs[0]
    ax.set_title(r'Mesurement model $p(Z_t|X_t)$')
    bar_plot(ax, x, y, color='r')

    # Motion model
    p = [0, 0.75, 0.25]
    y = np.array(p)
    x = np.arange(len(y))

    ax = axs[1]
    ax.set_title(r'Motion model $p(X_{t+1}|X_t)$')
    bar_plot(ax, x, y, color='b')
    ax.axvline(0.25, c='k', ls='--')
    ax.axvline(-0.25, c='k', ls='--')

    plt.show()


if __name__ == "__main__":
    # argparse
    cli_params = dict(
        task=0,
    )

    args = cli_args(cli_params)
    task = int(args['task'])

    # PDF as bar plot
    if task == 1:
        task_1()
    elif task == 2:
        task_2()
    elif task == 3:
        task_3()
