import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


frames = 1000 
fall_speed_initial = 2.5  
gravity = 0.01  
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

circle = plt.Circle((5, 10), 0.5, color='blue')
ax.add_artist(circle)


position = 10  # Начальная высота
velocity = fall_speed_initial  # Начальная скорость
time_step = 1/30  

def update(frame):
    global position, velocity
    
    velocity += gravity*time_step  
    position -= velocity*time_step  
    circle.set_center((5, position))
    return circle,
plt.axis('equal')
# Создаем анимацию
ani = FuncAnimation(fig, update, frames=frames, blit=True, repeat=False, interval=25)

ani.save("fall.gif", writer = 'pillow')
     
