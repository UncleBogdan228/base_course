import numpy as np
from constant import g
t = 5
xnull = int(input())
ynull= int(input())
vnull= int(input())
x = xnull + vnull*t
y = ynull + vnull*t - (g*t**2)/2
mass = np.zeros ((1,3))
mass[0,0] = t
mass[0,1] = x
mass[0,2] = y
print(mass)
