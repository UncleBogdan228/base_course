import numpy as np
M = int(input('Ведитеразмер массива (не более 10):'))
mass = np.zeros((1,M))
for i in range(0,M):
    el=int(input('Ведите элемент массива:'))
    mass[0,i] = el
print (mass)

new = int(input('Введите новый элемент:'))
poz1 = int(input('Введите позицию элемента:'))
poz = poz1 - 1
'''
mass = np.insert(mass,poz,new)
print(mass)
'''
newmass = np.zeros((1,M+1))
for i in range (0,poz):
    newmass[0,i] = mass[0,i]

newmass[0,poz] = new
for i in range (poz+1,M+1):
    newmass[0,i] = mass[0,i-1]
print(newmass)