import matplotlib.pyplot as plt
import numpy as np

def ellips (a = 100,b = 50):
    x = np.linspace(-100, 100, 100)
    y = np.linspace(-100, 100, 100)
    
    X, Y = np.meshgrid(x,y)
    fxy = X**2/a**2 + Y**2/b**2

    plt.contour(X,Y,fxy, levels=[1])
    plt.axis('equal')
    plt.savefig('task3.png')

if __name__ == '__main__':
    ellips()