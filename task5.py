a = int(input())
b = int(input())

if a == 0 or b == 0:
    print('на ноль делить низя')
elif a % b == 0:
    print('делится без остатка')
    print('частное =', a // b)
elif a % b != 0:
     print('делится с остатком')
     print('частное =', a // b)
     print('остаток =', a % b)




