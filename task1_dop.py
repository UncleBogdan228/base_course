import random
import time
a, b, c, d, e = random.random(), random.random(), random.random(), random.random(), random.random()

def uravnen (x):
    return a*x**4 + b*x**3 + c*x**2 + d*x + e

start_numsmap = time.time()
numsmap = list(map(uravnen, range(10**5)))
end_numsmap = time.time()
time_numsmap = end_numsmap - start_numsmap

start_numslist = time.time()
numslist = [uravnen(x) for x in range(10**5)]
end_numslist = time.time()
time_numslist = end_numslist - start_numslist

start_numsforin = time.time()
numsforin = []
for x in range (10**5):
    numsforin.append(uravnen(x))
end_numsforin = time.time()
time_numsforin = end_numsforin - start_numsforin

print('Время работы map:', time_numsmap)
print('Время работы спискового включения:', time_numslist)
print('Время работы цикла:', time_numsforin)
