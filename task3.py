import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def babachka (t, time):
    t = np.arange(0, 12*np.pi, 0.1) * time
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 2) ** 5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 2) ** 5)


    return x, y

t = np.arange(0, 12*np.pi, 300)
fig, ax = plt.subplots()
baba_line, = plt.plot([], [], '-', color='r', label='Baba')

frames=len(t)
coords = np.zeros((frames, 2))

def animate(i):
    x, y = babachka(t[:i+1], 1) 
    baba_line.set_data(x[:i], y[:i])
    return baba_line,

edge = 3
plt.axis('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

ani = FuncAnimation(fig, animate, frames=1000, interval=25)
ani.save('task3.gif', writer='pillow')