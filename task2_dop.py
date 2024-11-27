import matplotlib.pyplot as plt
import numpy as np

def spiral (a = 100, b = 50):
    f = np.linspace(0, 10*np.pi, 500)
    c = (a**2 - b**2)**0.5
    e = c/a
    p = a*(1 - e**2)
    r = p / (1 + e*np.cos(f))
    x = r * np.cos(f)
    y = r * np.sin(f)
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('task2_dop.png')


if __name__ == "__main__":
    spiral()