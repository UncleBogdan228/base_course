def mew(a,b):
    x = 3*a-b
    return x
#tmp = mew()

def mew(a=1,b=0):
    x = 3*a-b
    return x
print(mew())
print(mew(3,4))
print(mew(3))
print(mew(b=3))

def mu_func(a,b=0): #сначала идут без значений по умолчанию
    x = 3*a-b
    return x 

def my_func(*args): # * - бесконечная передача элементов, идет в конце
    x  = 3 * args[0] - args[1]
    return x 
print(my_func(3,4))
print(my_func(3,4,8))

def my_func(**kwrgs): # ** - запаковать словарь
    x = 3 * kwrgs['obj_1'] - kwrgs['obj_2']
    return x
print(my_func(obj_1=3, obj_2=4))