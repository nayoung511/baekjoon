n, f = map(int, input().split())

# 일단 f를 나눠보자
# n == 4 면 총 3개의 줄이 필요함
# 총 n-1개의 연산이 필요함

num = []
def solve(f):
    global num
    print(num)

    if len(num) == n:
        return

    if f % 2 == 0:
        num.append(f//2 -1)
        num.append(f//2 +1)
    else:
        num.append(f//2)
        num.append(f//2+1)

    for i in range (len(num)):
        solve(num[i])
        
        
solve(f)
print(num)