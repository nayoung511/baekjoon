n = int(input())

a = list(map(int, input().split()))

a.sort()
wait = sum(a)

for i in range (n-1, 0, -1):
    a.pop(i)
    wait += sum(a)

print(wait)