import time
M = 2
N = 3
start_time = time.time()
for i in range(M):
    time.sleep(1)
    print(i) 
    for i in range(N):
        time.sleep(1)
        print(i)

end_time=time.time()
print("Время выполнени:", end_time - start_time)
        
