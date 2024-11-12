
fig = str(input())
def pl(fig, *arg):
    if fig == 'круг':
        s = 3.14 * arg[0]**2
    if fig == 'прямоугольник':
        s = arg[0]*arg[1]
    if fig == 'треугольник':
        s = 0.5 * arg[0] * arg[1]
    return s

print(pl(fig,10,20))
    