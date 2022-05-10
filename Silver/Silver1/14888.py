import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split()) # +, -, x, /

# maxx를 sys상 가장 최솟값
# minn을 sys상 가장 최댓값
maxx, minn = -sys.maxsize -1, sys.maxsize

def solve(k, summ1, add, sub, mul, div):
    global maxx, minn

    if k == n:
        maxx = max(summ1, maxx)
        minn = min(summ1, minn)
        return

    if add > 0:
        solve(k+1, summ1 + num[k], add - 1, sub, mul, div)
    if sub > 0:
        solve(k+1, summ1 - num[k], add, sub-1, mul, div)
    if mul > 0:
        solve(k+1, summ1 * num[k], add, sub, mul-1, div)
    if div > 0:
        solve(k+1, int(summ1 / num[k]), add, sub, mul, div-1)


solve(1, num[0], add, sub, mul, div)

print(maxx)
print(minn)
