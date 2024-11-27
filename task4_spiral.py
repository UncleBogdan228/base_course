import matplotlib.pyplot as plt
import numpy as np

def spiral (a=1, b=0.2):
    f = np.linspace(0, 10*np.pi, 500)
    r = a * np.exp(b * f)
    x = r * np.cos(f)
    y = r * np.sin(f)
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('task4_spiral.png')


if __name__ == "__main__":
    spiral()