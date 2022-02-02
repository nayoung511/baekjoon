from sys import stdin

n = int(input())
arr = list(map(int, stdin.readline().split()))

m = int(input())

#sum
index_sum = [0] * (n+1)
for i in range (1, n+1):
    index_sum[i] = index_sum[i-1] + arr[i-1]

#print(index_sum)

for _ in range (m):
    start, end = map(int, stdin.readline().split())
    #print(index_sum[end], index_sum[start-1])
    print(index_sum[end] - index_sum[start-1])
