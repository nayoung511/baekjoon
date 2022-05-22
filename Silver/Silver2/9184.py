import sys
input = sys.stdin.readline

a = [-1, -1, -1]

def calculate(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        calculate(20, 20, 20)
    elif a < b and b < c:
        calculate(a, b, c-1) + calculate(a, b-1, c-1) + calculate(a, b-1, c)
    else:
        calculate(a-1, b, c) + calculate(a-1, b-1, c) + calculate(a-1, b, c-1) - calculate(a-1, b-1, c-1)

while True:
    num = list(map(int, input().split()))
    if num == a:
        break
    else:
        print(calculate(num[0], num[1], num[2]))


    