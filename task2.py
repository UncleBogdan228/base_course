import numpy as np
from constant import g
h = 100
a = 45
b  = 35
v = ((g*h*np.tan(b)**2) / (2*np.cos(a)**2 * (1 - np.tan(b) * np.tan(a))))**0.5
print(v)