import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() #пространство и подпространство для анимации
anim_object, = plt.plot ([], [], '-', lw=2) #объект анимации
x, y = [], []
parametr = np.linspace(0, 2*np.pi, 100)
ax.set_xlim(0,2*np.pi) #пределы изменения х
ax.set_ylim(-1,1)#пределы изменения у

#функция подстановки параметра в объект анимации
def update (frame):
    x.append(frame)#расчет координаты х 
    y.append(np.sin(frame))#расчет координаты у

    #передача координат объекту анимации
    anim_object.set_data(x,y)

    return anim_object

ani = FuncAnimation(fig, #вызов пространства для анимации
                     update, #вызов функции подстановки координат
                       frames = parametr, #интервал значений 
                         interval = 50) #интервал между кадрами
ani.save('animation_1.gif', writer='pillow')

