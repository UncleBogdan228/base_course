import matplotlib.pyplot as plt
import numpy as np

def arhspiral (a = 1):
    f = np.linspace(0, 8*np.pi, 100)
    r = a * f
    x = r * np.cos(f)
    y = r * np.sin(f)
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('task4_arhspiral.png')



if __name__ == '__main__':
    arhspiral()