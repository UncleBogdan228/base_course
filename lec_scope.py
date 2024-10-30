x0= 10# Переменная в глобальной области видимости
def move(t):
    x = x0*t #локальная область видимости
    return x
print(move(3))
#print(x) ашибка
a = 'Good'
def mew():
    a = 'bad'
    print(a)
mew()
print(a)