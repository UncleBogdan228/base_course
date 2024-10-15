a = int(input())
b = int(input())
c = int(input())
if b**2 - 4*a*c < 0:
    print('нет корней')
if b**2 - 4*a*c == 0:
    print('один корень')
    print(-b / 2*a)
if b**2 - 4*a*b > 0:
    print('два корня')
    print((-b + ((b**2 - 4*a*c) ** 0.5)) / (2*a))
    print((-b - ((b**2 - 4*a*c) ** 0.5)) / (2*a))


