from skylynx.utils import cli_args
from utils import *
import matplotlib.pyplot as plt
import numpy as np


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
