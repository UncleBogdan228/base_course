import numpy as np
n = int(input('Введите количество строк:'))
m = int(input('Введите количество столбцов:'))
mass  = np.zeros((n,m))
for i in range (0,n):
    for j in range (0,m):
        elem = np.sin(n * i + m * j + 1)
        if elem >= 0:
            mass[i,j] = elem
        else: 
            mass[i,j]=0
print(mass)
