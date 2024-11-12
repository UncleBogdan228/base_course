a = int(input())
n = int(input())
def step (a,n):
    if n == 0:
        return 1
    if n < 0:
        astep=1
        for i in range(-n):
            astep = astep * a
        return 1/astep
    else:
        astep = 1
        for i in range (n):
            astep = astep*a
        return astep
print(step(a,n))