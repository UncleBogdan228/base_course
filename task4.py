import matplotlib.pyplot as plt
import numpy as np

def spiral (a=1, b=0.2):
    f = np.linspace(0, 8*np.pi, 10)
    r = a ** (b ** f)
    x = r * np.cos(f)
    y = r * np.sin(f)
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('task4_spiral.png')

def arhspiral (a = 1):
    f = np.linspace(0, 8*np.pi, 100)
    r = a * f
    x = r * np.cos(f)
    y = r * np.sin(f)
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('task4_arhspiral.png')

def gesl (a = 1):
    f = np.linspace(0, 100, 100)
    r = a / (f**0.5)
    x = r * np.cos(f)
    y = r * np.sin(f)
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('task4_gesl.png')


if __name__ == '__main__':
    spiral()
    arhspiral()
    gesl()