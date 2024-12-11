import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from constans import e

fig, ax = plt.subplots() 
anim_object, = plt.plot ([], [], '-', lw=2) 
# x, y = [], []
parametr = np.linspace(0, 10, 100)
ax.set_xlim(-5,5) 
ax.set_ylim(-5,5)

def update (t, time=parametr):
    t = np.arange(0, 12*np.pi, 0.1) * time
    x = np.sin(t) *(e**np.cos(t)-2*np.cos(4*t) + np.sin(t/2)**5)
    y = np.cos(t) *(e**np.cos(t)-2*np.cos(4*t) + np.sin(t/2)**5)

    
    anim_object.set_data(x,y)

    return anim_object

ani = FuncAnimation(fig, update, frames = parametr, interval = 50) 
ani.save('task3.gif', writer='pillow')


'''
def babachka (t, time):
    t = np.arange(0, 12*np.pi, 0.1) * time
    x = np.sin(t) *(e**np.cos(t)-2*np.cos(4*t) + np.sin(t/2)**5)
    y = np.cos(t) *(e**np.cos(t)-2*np.cos(4*t) + np.sin(t/2)**5)
    

    return x, y

fig, ax = plt.subplots()
baba, = plt.plot([], [], 'o', color='r', label='Baba')
baba_line, = plt.plot([], [], '-', color='r', label='Baba')

frames = 180
coords = np.zeros((frames, 2))

def animate(i):
    coords[i] = babachka(time=i )
    baba.set_data([coords[i][0]], [coords[i][1]])
    baba_line.set_data(coords[:i, 0], coords[:i, 1])
    return baba, baba_line

edge = 3
plt.axis('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

ani = FuncAnimation (fig, animate, frames=100, interval = 30)
ani.save('task3.gif', writer='pillow')
'''