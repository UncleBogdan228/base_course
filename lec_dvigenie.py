import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def circle_move(R, Vxo, Vyo, time):
    x0 = Vxo *time
    y0 = Vyo * time
    alpha = np.arange(0,2*np.pi,0.6)
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x,y

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')

def animate (i):
    ball.set_data(circle_move(R=0.5, Vxo=0.01, Vyo=0.01, time=i))
    return ball

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation (fig, animate, frames=100, interval = 30)
ani.save('animation_3.gif', writer='pillow')