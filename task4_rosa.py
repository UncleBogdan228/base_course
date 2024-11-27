import matplotlib.pyplot as plt
import numpy as np

def rosa (k = 3):
    f = np.linspace(0, 10*np.pi, 500)
    r = np.sin(k * f)
    x = r * np.cos(f)
    y = r * np.sin(f)
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('task4_rosa.png')

'''
def rosa2 (k = 0.5):
    f = np.linspace(0, 10*np.pi, 500)
    r = np.sin(k * f)
    x = r * np.cos(f)
    y = r * np.sin(f)
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('task4_rosa.png')
'''

if __name__ == "__main__": 
    #rosa2()
    rosa()