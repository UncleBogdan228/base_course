import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

A1 = 1.0  
f1 = 1.0  
A2 = 0.7  
f2 = 2.0  

frames = 100
interval = 50

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)

line1, = ax.plot([], [], color='b', lw=2) 
point1, = ax.plot([], [], 'o')
line2, = ax.plot([], [], color='g', lw=2) 
point2, = ax.plot([], [], 'o')  


def animate(i):
    t = np.linspace(0, 10 * i / frames, 100) 
    
    y1 = A1 * np.sin(2 * np.pi * f1 * t)
    line1.set_data(t, y1)
    point1.set_data([t[-1]], [y1[-1]])
    
    y2 = A2 * np.sin(2 * np.pi * f2 * t)
    line2.set_data(t, y2)
    point2.set_data([t[-1]], [y2[-1]]) 


    return line1, point1, line2, point2,


ani = FuncAnimation(fig, animate, frames=frames, interval=interval)
ani.save('task2_dop.gif', writer='pillow')
