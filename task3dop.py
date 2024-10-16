a = int(input('введите число:'))
y = str(a)
z = "" 

for i in range(len(y) - 1, -1, -1):
    z = z + y[i]
print(z)
#a = int(z)

