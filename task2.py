b1 = int(input('Введите первый член прогрессии:'))
znam = int(input('Введите знаменатель:'))
kol = int(input('Введите количество членов прогрессии:'))

for i in range(1, kol + 1 ):
    print((b1 * znam ** (i-1)))