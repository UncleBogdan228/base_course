import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

R = 1
t = np.linspace(0, 4 * np.pi, 200)  

x = R * (t - np.sin(t))
y = R * (1 - np.cos(t))

fig, ax = plt.subplots()
ax.set_xlim(-1, 4 * np.pi + 1)
ax.set_ylim(-1, 2.5 * R)    
ax.set_aspect('equal') 
ax.plot(x, y, color='b')
point, = ax.plot([], [], 'o', color='r')

def animate(i):
    point.set_data([x[i]], [y[i]]) 
    return point,


ani = FuncAnimation(fig, animate, frames=len(t), interval=50)
ani.save('task1_dop_cik.gif', writer='pillow')
