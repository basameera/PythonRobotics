import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from utils import gen_pdf

"""
# TODO: Need to learn how `norm.fit()` work -> maximum likelihood

Automatic sensor modeling flow:
1. Move to a random position in space
2. Take 200 samples (dataset)
3. Using `norm.fit()` to estimate mu, std
4. Do steps 1. to 3. for two more different random positions in space. (Now there's three mu values and std values)
5. Get the avg. of all std values as the model parameter
6. using this `std`, do `norm.fit()` again to refine the mu estimates.

"""

if __name__ == "__main__":
    np.random.seed(123)

    # ** Model the sensor **

    mu, sigma = 20, 1  # mean and standard deviation

    sigma = sigma

    s = np.random.normal(mu, sigma, 200)

    bins = np.arange(-3, 3 + 2) - 0.5
    bins += mu
    print(bins)

    x_pos = np.linspace(-3, 3, 100)
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

    color = 'red'
    # we already handled the x-label with ax1
    ax2.set_ylabel('Probability', color=color)
    ax2.plot(x_pos, pdf, color=color,
             label='Ideal model P() - $N(\mu={},\sigma={})$'.format(mu, sigma))
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.legend()

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.savefig('sm_ideal.pdf')
    # plt.show()
    plt.close()

    # ** acquire synthetic samples from the sensor
    n_samples = 200
    mesurement = 50
    std = sigma
    sensor_data = np.random.normal(mesurement, std, n_samples)

    # set sensor resolution to 1 cm
    sensor_data = np.round(sensor_data)

    bins = np.arange(-3, 3 + 2) - 0.5
    bins = bins
    bins += mesurement

    bin_pos = np.arange(-3, 3+1) + mesurement
    print(bin_pos)

    fig, axs = plt.subplots(1, 2)
    fig.suptitle('Sensor mesurements')
    ax = axs[0]

    count, bins, ignored = ax.hist(sensor_data, bins)

    print(np.min(sensor_data))

    ax.set_title('Frequency')

    ax.set_axisbelow(True)
    ax.grid()

    ax = axs[1]
    prob = count/n_samples
    ax.bar(bin_pos, prob)

    mu_est, sigma_est = norm.fit(sensor_data)
    mu_est = np.round(mu_est)
    sigma_est = np.round(sigma_est)

    x_pos = np.linspace(-3, 3, 100) + mesurement

    ax.plot(x_pos, gen_pdf(x_pos, mu_est, sigma_est), c='r',
            label='Ideal model P() - $N(\mu={},\sigma={})$'.format(mu_est, sigma_est))

    ax.legend()
    ax.set_axisbelow(True)
    ax.grid()
    ax.set_title('Probability')
    ax.set_xlabel('Z (cm)')

    plt.show()
