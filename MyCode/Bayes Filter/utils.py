import numpy as np


def gen_pdf(x, mu=0.0, sigma=1.0):
    r"""[summary]

    Parameters
    ----------
    x : [type]
        [description]
    mu : float, optional
        [description], by default 0.0
    sigma : float, optional
        [description], by default 1.0

    Returns
    -------
    [type]
        [description]
    """    
    return 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(- (x - mu)**2 / (2 * sigma**2))


def bar_plot(ax, x, y, color=None, label=''):
    r"""Bar Plot

    Parameters
    ----------
    x : 1D array

    y : 1D array

    """

    # ax.set_axisbelow(True)
    # ax.grid(ls='--')
    ax.bar(x, y, color=color, width=0.5, label=label)
    # plt.xlabel("File names")
    # plt.ylabel("Execution time (seconds)")
    # plt.title("Effects of Numba (loop of 1e6)")
    # plt.xticks(x_pos, x)
    # plt.savefig('stats.pdf')
    # ax.set_ylim(0, 1)


def norm(x):
    """Normalize array

    Parameters
    ----------
    x : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    x = np.array(x)
    if int(np.sum(x)) != 1:
        x = x/np.sum(x)
    return x


if __name__ == "__main__":
    pass
