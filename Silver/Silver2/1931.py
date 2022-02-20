from sys import stdin

n = int(input())
arr = [0] * (n)
for i in range (n):
    arr[i] = list(map(int, stdin.readline().split()))

arr.sort(reverse = True)

link = []
start, end = arr[0][0], arr[0][0]

arr.remove(arr[0])
for time in arr:
    if time[1] <= start:
        start = time[0]
        link.append(time)
    #print(arr)

print(len(link) + 1)