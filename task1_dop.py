import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

R = 1
t = np.linspace(0, 2 * np.pi, 200) 
x = R * np.cos(t)**3
y = R * np.sin(t)**3

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.2*R, 1.2*R)  
ax.set_ylim(-1.2*R, 1.2*R)  
ax.set_aspect('equal')
ax.plot(x, y, label='Астроида', color='blue')
point, = ax.plot([], [], 'o', color='r')

def animate(i):
    point.set_data([x[i]], [y[i]])
    return point,


ani = FuncAnimation(fig, animate, frames=len(t), interval=50)
ani.save('task1_dop_ast.gif', writer='pillow')