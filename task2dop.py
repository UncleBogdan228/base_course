a = int(input())
b = int(input())
c = int(input())
if b**2 - 4*a*b < 0:
    print('нет корней')
if b**2 - 4*a*b == 0:
    print('один корень')
    print(b*(0-1) / 2*a)
if b**2 - 4*a*b > 0:
    print('два корня')
    print((b * (0-1)) + ((b**2 - 4*a*b) ** 1/2)) / (2*a) 
    print((b* (0-1)) - ((b**2 - 4*a*b) ** 1/2)) / (2*a)


