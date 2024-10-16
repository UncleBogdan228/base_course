import numpy as np
a = [1, 2, 3]
b = np.array(a) #создание массива из списка
print(type(a))
print(type(b))

print(b * b)
print(b/b)
print(b-b)

c = np.append(b, 'good')
print(c)

print(b[-1])
print(a[-1])