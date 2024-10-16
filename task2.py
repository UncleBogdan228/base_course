import numpy as np
import constant 
h = 100
a = 45
b  = 35
g = constant.g

v = (g*h*np.tan(b)**2 / ((2*(np.cos(a)**2)) * (1 - np.tan(b) * np.tan(a))))**0.5
print(v)