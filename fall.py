import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Настроим параметры анимации
frames = 1000  # Увеличиваем количество кадров
fall_speed_initial = 2  # Уменьшаем начальную скорость
gravity = 0.01  # Уменьшаем ускорение свободного падения

# Определим фигуру и оси
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Создаем кружок
circle = plt.Circle((5, 10), 0.5, color='blue')
ax.add_artist(circle)

# Начальные параметры
position = 10  # Начальная высота
velocity = fall_speed_initial  # Начальная скорость
time_step = 1/30  # Шаг по времени (примерно 30 кадров в секунду)

def update(frame):
    global position, velocity
    # Обновляем скорость и позицию кружка
    velocity += gravity*time_step  # Увеличиваем скорость из-за "гравитации"
    position -= velocity*time_step  # Обновляем позицию
    circle.set_center((5, position))
    if position < 0:  # Предотвращаем падение ниже оси
        position = 0
        velocity = 0
    return circle,

# Создаем анимацию
ani = FuncAnimation(fig, update, frames=frames,interval=25, blit=True, repeat=False)

ani.save("fall.gif", writer = 'pillow')
# Показываем анимацию

 
     
