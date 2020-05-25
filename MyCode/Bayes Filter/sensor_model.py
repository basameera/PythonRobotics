import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    np.random.seed(123)

    # ** Model the sensor **

    mu, sigma = 100, 1  # mean and standard deviation

    factor = 1
    sigma = sigma / factor

    s = np.random.normal(mu, sigma, 200)

    bins = np.arange(-3, 3 + 2) - 0.5
    bins = bins/factor
    bins += mu
    print(bins)

    x_pos = np.linspace(-3, 3, 100)
    x_pos = x_pos/factor
    x_pos += mu

    # dual

    fig, ax1 = plt.subplots()
    plt.title('Ideal model')

    color = 'blue'
    ax1.set_axisbelow(True)
    ax1.grid(axis='x')
    ax1.set_xlabel('Sample (cm)')
    ax1.set_ylabel('Frequency', color=color)
    count, bins, ignored = ax1.hist(s, bins, density=False, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    # ax2.set_axisbelow(True)
    ax2.grid(axis='y')

    pdf = 1/(sigma * np.sqrt(2 * np.pi)) * \
        np.exp(- (x_pos - mu)**2 / (2 * sigma**2))
    pdf /= factor

    color = 'red'
    # we already handled the x-label with ax1
    ax2.set_ylabel('Probability', color=color)
    ax2.plot(x_pos, pdf, color=color,
             label='Ideal model P() - $N(\mu={},\sigma={})$'.format(mu, sigma))
    ax2.tick_params(axis='y', labelcolor=color)
    # ax2.set_ylim(0, 41.85)
    ax2.legend()

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()

    # ** acquire synthetic samples from the sensor
    s = np.random.normal(mu, sigma, 100)
