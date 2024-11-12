import numpy as np
a = int(input())
b = int(input())
N = int(input())
x = np.linspace(a,b,N)
print(x)
def func (a):
    for i in range(0,len(x)):
        x[i] = x[i] ** 2
    return x
print(func(x))
    

    
    