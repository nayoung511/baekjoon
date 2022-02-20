n = int(input())
num = list(map(int, input().split()))
x = int(input())

count = 0
num.sort()
start, end = 0, len(num) - 1

while(start != end):
    if num[start] + num[end] == x:
        count+=1
        start +=1
    elif (num[start] + num[end]) > x:
        end -= 1
    else:
        start += 1

print(count)