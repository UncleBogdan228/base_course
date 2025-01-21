import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math
from matplotlib.path import Path #прикол чтобы норм замкнутые линии были отрисовывались, а не как кишмиш
import matplotlib.patches as patches #таже херь


frames = 1000
fall_speed = 1 #начальная скорость падения
gravity = 0.01 
rotation_speed = 0.01 # Угловая скорость вращения


fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 12)
ax.set_aspect('equal')  # типо плт аксис чтобы нормално выглядело

# функция для создания кривой Коха
def koch_curve(p, q, n, lines=None):
    if lines is None:
         lines = []
    if n == 0:
        lines.append(p)
        lines.append(q)
    else:
        v = q - p
        lines = koch_curve(p, p + v / 3, n - 1, lines)
        R_60 = np.array([[math.cos(math.pi / 3), -math.sin(math.pi / 3)],
                          [math.sin(math.pi / 3), math.cos(math.pi / 3)]])
        x = p + v / 3 + R_60 @ (v / 3)
        lines = koch_curve(p + v / 3, x, n - 1, lines)
        lines = koch_curve(x, p + 2 * v / 3, n - 1, lines)
        lines = koch_curve(p + 2 * v / 3, q, n - 1, lines)
    return lines

def koch_snowflake(n):
    p = np.array([[0], [0]])
    q = np.array([[1], [0]])
    r = np.array([[0.5], [math.sqrt(3) / 2]])
    
    lines = koch_curve(p, r, n)
    lines = np.concatenate((lines, koch_curve(r, q, n)))#херня чтобы не расползлась опять как тварь
    lines = np.concatenate((lines, koch_curve(q, p, n)))

    return np.array(lines).reshape(-1, 2)

# создаем снежинку 
snowflake_points = koch_snowflake(2)

# чтобы найти границы 
x_coords = snowflake_points[:, 0]
y_coords = snowflake_points[:, 1]

min_x, max_x = min(x_coords), max(x_coords)
min_y, max_y = min(y_coords), max(y_coords)

# чтобы центр найти у снежинки
center_x = (min_x + max_x) / 2
center_y = (min_y + max_y) / 2
width = max_x - min_x
height = max_y - min_y

# сдвигаем снежинку к центру
scale = 1.5 / max(width, height) #найти масштаб чтобы поместилась в оси
snowflake_points[:, 0] = (snowflake_points[:, 0] - center_x) * scale
snowflake_points[:, 1] = (snowflake_points[:, 1] - center_y) * scale

# короче сливаем все воедино в патч чтобы была ну пряма фигура класс супер ого
codes = [Path.MOVETO] + [Path.LINETO] * (len(snowflake_points) - 1)
snowflake_path = Path(snowflake_points, codes)

# чтобы был объект и отображался
snowflake_patch = patches.PathPatch(snowflake_path, facecolor='none', edgecolor='k')# заливка и контур
ax.add_patch(snowflake_patch)

# начальные параметры
position = 10  # начальная высота
velocity = fall_speed # нач скорость
angle = 0 # нач угол поворота
time_step = 1/30 # временной шаг

def update(frame):
    global position, velocity, angle
    velocity += gravity * time_step
    position -= velocity * time_step
    angle += rotation_speed

    # Вращение и сдвиг
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle), np.cos(angle)]]) #кекнутая матрица поворота на текущий угол
    rotated_points = np.dot(snowflake_points, rotation_matrix)
    rotated_points[:, 1] += position

    # короче чтобы с патчем вертелась и летела нормально
    codes = [Path.MOVETO] + [Path.LINETO] * (len(snowflake_points) - 1)
    snowflake_path_new = Path(rotated_points, codes)
    snowflake_patch.set_path(snowflake_path_new)

    return [snowflake_patch]

ani = FuncAnimation(fig, update, frames=frames, blit=True, repeat=False, interval=25)

ani.save("snowflake_fall.gif", writer='pillow')
