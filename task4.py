import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x0 = 0.1
y0 = 0.1
C = 0.3
D = 0.33
num = 500 

def point(xm, ym, C, D):
    x = xm**2 - ym**2 + C
    y = 2 * xm * ym + D
    return x, y

x_coords = [x0]
y_coords = [y0]

for _ in range(num - 1):
    x_next, y_next = point(x_coords[-1], y_coords[-1], C, D)
    x_coords.append(x_next)
    y_coords.append(y_next)

fig, ax = plt.subplots()
ax.set_xlim([-0.1, 1]) 
ax.set_ylim([-0.1, 1])
line, = plt.plot([], [], '-', color='r')
plt.axis('equal')

def animate(i):
    line.set_data(x_coords[:i+1], y_coords[:i+1])
    return line,

ani = FuncAnimation(fig, animate, frames=num, interval=25)
ani.save('task4.gif', writer='pillow')