import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def heart (t, time):
    t = np.linspace(0, 2 * np.pi) * time
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)


    return x, y

t = np.arange(0, 2 * np.pi)
fig, ax = plt.subplots()
heart_line, = plt.plot([], [], '-', color='r', label='heart')

frames=len(t)
coords = np.zeros((frames, 2))

def animate(i):
    x, y = heart(t[:i+1], 1) 
    heart_line.set_data(x[:i], y[:i])
    return heart_line,

edge = 3
plt.axis('equal')
ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)

ani = FuncAnimation(fig, animate, frames=1000, interval=25)
ani.save('task3_serdechko.gif', writer='pillow')