from constans import g
def energ(m, h, v):
    ekin = m*v**2/2
    epot = m*g*h
    e = epot + ekin
    return (e)

print(energ(100,1000,99))