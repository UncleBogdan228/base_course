import numpy as np
from constant import g
#t = int(input('Введите начальное время от 0 до 5 секунд:'))
xnull = int(input('Введите начальную  координату по х:'))
ynull= int(input('Введите начальную координату по у:'))
vnull= int(input('Введите начальную скорость:'))
for i in np.linspace(0,5,100):
    t = i
    x = xnull + vnull*t
    y = ynull + vnull*t - (g*t**2)/2
    mass = np.zeros ((1,3))
    mass[0,0] = t
    mass[0,1] = x
    mass[0,2] = y
    print(mass)

