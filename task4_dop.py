import matplotlib.pyplot as plt
import numpy as np

N = int(input())
langs = 1
width = 1
def lesenk (N):
    x = []
    y = []
    xstart = 0
    ystart = 0
    for i in range (N):
        x.append(xstart)
        x.append(xstart)
        y.append(ystart)
        y.append(ystart + width)
        ystart = ystart + langs
        plt.plot(x,y)

        x.append(xstart) 
        x.append(xstart + langs)
        y.append(ystart)
        y.append(ystart)
        xstart = xstart + width
        plt.plot(x,y)
    

    plt.axis('equal')
    plt.savefig('task4_dop.png')

if __name__ == "__main__":
    lesenk(N)
'''
x = np.linspace(0,10,1000)
y = x // 1
'''
