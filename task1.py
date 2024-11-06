import numpy as np
a = [8, 9, 10, 5, 7]
mass =  np.array(a)

def sr(a):
    for i in a:

    return sum(a)/len(a)
print(sr(mass))

def sred (*args):
    return sum(args)/len(args)
print(sred(1, 4, 8, 9, 5, 4))