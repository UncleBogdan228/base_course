import matplotlib.pyplot as plt
import numpy as np

def astr(R=10):
    t = np.arange(-10, 10, 0.01)

    x = R * np.cos(t) ** 3
    y = R * np.sin(t) ** 3 

    plt.plot(x, y, ls='-', lw = 1)
    plt.axis('equal')
    plt.savefig('task1_astroida.png')

if __name__ == "__main__":
    astr()