def changer(a,b):
    a = 2
    b[0] = 'god'

x = 10
L = [1,2]
changer(x,L)
print(x)
print(L)

L = [1,2]
changer(x, L[:])
print(L)

#COMPLEX

x = 3
y = 4
z = complex(x,y)
print(z)
w = complex(y, x)
print(z + w)

#STRINGS

s = 'hello'
print(s[0])
#s[0] = 'H' ашибка

#TUPLE

t = (1, 4, 9)
print(t)
print(t[0])
#t[0] = 3 ашибка

#DICT

d = {'al':4, 4:'al', 'str':'Hello'}#ключ знач
print(d['al'])
d['str'] = 'Good'
print(d)