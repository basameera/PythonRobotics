import numpy as np

np.random.seed(123)

def create_toy_data(ly, std):
    t = ly + np.random.normal(scale=std, size=ly.shape)
    return t


if __name__ == "__main__":
    pass
