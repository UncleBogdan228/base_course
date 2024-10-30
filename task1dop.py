import numpy as np
N = int(input('Введите длину массивов:' ))
M = int(input('Введите ширину массивов:'))
mass1 = np.zeros((N,M))
mass2= np.zeros((N,M))
mass3 = np.zeros((N,M))

for i in range (0,N):
    for j in range (0,M):
        el = int(input('Введите элемент первого массива:'))
        mass1[i,j] = el

for i in range (0,N):
    for j in range (0,M):
        el = int(input('Введите элемент второго массива:'))
        mass2[i,j] = el

for i in range (0,N):
    for j in range (0,M):
        if mass1[i,j] > mass2 [i,j]:
            mass3[i,j]=mass1[i,j]
        elif mass2 [i,j] > mass1[i,j]:
            mass3[i,j]=mass2[i,j]
        elif mass1[i,j]==mass2[i,j]:
            mass3[i,j]=mass1[i,j]
print(mass1)
print(mass2)
print(mass3)