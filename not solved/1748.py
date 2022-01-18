n = input()
num = list(map(int, n))

if len(n) == 1:
    print(n)

else:
    #본인
    sum = len(n) + 9
    for i in range (len(n)):
        sum += (num[i]) * len(n) * 10
        
print(sum)