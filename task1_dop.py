import matplotlib.pyplot as plt
import numpy as np

def lissaju (bet = np.pi/2, a =1, A = 1, B = 1, b = 1):
    t = np.linspace(0, 50, 50)
    x = A * np.sin(a * t + bet)
    y = B * np.sin(b * t)
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('task1_dop.png')


if __name__ == "__main__":
    lissaju()