import sys
n, m = sys.stdin.readline().split()
n, m = int(n), int(m)
num = sys.stdin.readline().split()
acc_sum = [0] * (n+1)

#누적 합
for i in range (1, n+1):
    acc_sum[i] = acc_sum[i-1] + int(num[n-i])
for i in range (m):
    start, end = sys.stdin.readline().split()
    start, end = int(start), int(end)
    print(acc_sum[n-start+1] - acc_sum[n-end])

