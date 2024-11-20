import matplotlib.pyplot as plt
import numpy as np

def giperbola (k=1):
    x = np.linspace(-100, 100, 100)
    y = k/x
    plt.plot(x,y)
    #plt.axis('equal')
    plt.savefig('task2.png')

if __name__ == '__main__':
    giperbola()