def solve(k):
    global cnt
    global num
    global equation
    #n 이 될 때까지 확인
    if k == n:
        equation.append(num)

        if cnt == m:
            for i in range (len(num)-1):
                print(num[i], "+", end='', sep='')
            print(num[-1])
        cnt+=1

    for i in range (1, 4):
        if k + i <= n:
            num.append(i)
            solve(k+i)
            num.pop()

equation = []
n, m = map(int, input().split())
num = []
cnt = 1

solve(0)

if m > len(equation):
    print(-1)