import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation



fig, ax = plt.subplots() 
anim_object, = plt.plot ([], [], '-', lw=2) 
# x, y = [], []
parametr = np.linspace(0, 10, 100)
ax.set_xlim(-10,10) 
ax.set_ylim(-10,10)

def update (frame):
    t = np.arange(-2*np.pi, 2*np.pi, 0.1)
    x = frame * np.cos(t)
    y = (frame * np.sin(t))

    
    anim_object.set_data(x,y)

    return anim_object

ani = FuncAnimation(fig, update, frames = parametr, interval = 50) 
ani.save('task2.gif', writer='pillow')
