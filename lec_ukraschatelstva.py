import matplotlib.pyplot as plt

x = [3, 8, 5]
y = [7, 4, 9]
plt.plot (x, y, color='g', label='Graf 1', marker='*', ms=5)
plt.plot (y, x,  color='r', label='Graf 2', marker='o', ms=3) #lable -  название, marker - пометка точки, ms - размер маркера

#---Украшательства---
plt.xlabel('Coord: x')#подпись ох
plt.ylabel('Coord: y')#подпись оу
plt.legend()#вызов легенды
plt.title('Base')#общая подпись
plt.grid()#подключение сетки
plt.savefig('fig_2.png')