import sys
input = sys.stdin.readline

money = []

n, m = map(int, input().split())
for i in range (n):
    money.append(int(input()))

start, end = min(money), sum(money)

while end >= start:
    mid = (end + start) // 2
    value = mid
    count = 1

    for i in range (n):
        if value < money[i]:
            value = mid
            count += 1
        value -= money[i]

    
    if count > m or mid < max(money):
        start = mid + 1
    else:
        end = mid - 1
        ans = mid

print(ans)


    


