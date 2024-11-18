import random

N = 10 
random1 = 0 
random2 = 100 

mass1 = [random.randint(random1, random2) for i in range(N)]
mass2 = [random.randint(random1, random2) for i in range(N)]
mass3 = [random.randint(random1, random2) for i in range(N)]
print(mass1)
print(mass2)
print(mass3)
max =max(max(mass1),max(mass2),max(mass3))
print('Максимальное число:', max)
summall = sum(mass1) + sum(mass2) + sum(mass3)
print('Сумма:', summall)

