import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split()) # +, -, x, /

# maxx를 sys상 가장 최솟값
# minn을 sys상 가장 최댓값
maxx, minn = -sys.maxsize -1, sys.maxsize

def solve(k, summ1, mul, div, add, sub):
    global maxx, minn

    if k == n:
        maxx = max(summ1, maxx)
        minn = min(summ1, minn)
        return

    if mul > 0:
        solve(k+1, summ1 * num[k], mul-1, div, add, sub)
    if div > 0:
        solve(k+1, int(summ1 / num[k]), mul, div-1, add, sub)
    if add > 0:
        solve(k+1, summ1 + num[k], mul, div, add-1, sub)
    if sub > 0:
        solve(k+1, summ1 - num[k], mul, div, add, sub-1)

for i in range (n):
    solve(1, num[i],  mul, div, add, sub)
    print(i, "--------")
    print(maxx)
    print(minn)