from task4 import mass 
stolb1 = int(input('Введите 1 стобец:'))
stolb2 = int(input('Введите 2 столбец:'))
slice1 = mass [::,stolb1-1]
for e in range (0,len(slice1)):
    temp = mass[e,stolb1-1]
    mass[e,stolb1 - 1] = mass[e, stolb2 - 1]
    mass[e, stolb2 - 1] = temp

print(mass)
