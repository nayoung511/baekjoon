from sys import stdin

def gcd(a, b): 
    if a == 0 :
        return b 
      
    return gcd(b%a, a)

n = int(input())

num = [0] * n

for i in range (n):
    num[i] = list(map(int, stdin.readline().split()))
    sum = 0
    print(num)
    start = 1
    end = 2
    flag = True
    m = num[i][0]

    while(start <= end and start < m):
        print(num[i][start], num[i][end])
        sum += gcd(num[i][start], num[i][end])
        print(start, end)
        print(sum, '\n')

        if end < m:
            print("here")
            end+= 1
        elif end == m :
            print("hi")
            start += 1
            end = start + 1
        elif start == m-1:
            break

        print(start, end)
    

    print("sum:", sum)