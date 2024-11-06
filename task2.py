import numpy as np 
b = [1, 77, 8, 9, 40, 5, 10]
mass = np.array(b)
def mnog(a):
    tmp = 1
    
    for i in a:
    
        tmp = tmp * i
        #a[i+1] = a[i] * a[i + 1]
    return(tmp)
        
print(mnog(mass))
