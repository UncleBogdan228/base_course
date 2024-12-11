import matplotlib.pyplot as plt
import numpy as np

def cikl(R=10):
    t = np.arange(-10, 10, 0.01)

    x = R * (t - (np.sin (t)) ** 3)
    y = R * (1 - (np.cos (t)) ** 3) 

    plt.plot(x, y, ls='-', lw = 1)
    plt.axis('equal')
    plt.savefig('task1_cikloida.png')

if __name__ == "__main__":
    cikl()