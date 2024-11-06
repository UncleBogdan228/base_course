import numpy as np
a = int(input())
b = int(input())
N = int(input())
x = np.linspace(a,b,N)
def func (a):
    y = x**2
    return y
print(func(x))
    

    
    