num = int(input())
if num == 1:
    print(1)

for i in range (2, num + 1):
    if num % i == 0 and i % 4 != 0:
        print(i)
        num = num / i
        for b in range(i):
            if num % i == 0:
                print(i)
    elif i + 1 == num:
        print(1)




 
