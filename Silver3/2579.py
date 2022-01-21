n = int(input())
step = [0]
for _ in range (n):
    step.append(int(input()))

g = [0, 0]
h = [0, step[1]]
for i in range (2, n+1):
    g.append(h[i-1] + step[i])
    h.append(max(g[i-2], h[i-2]) + step[i])

print(max(g[n], h[n]))
    

"""
    10  20  15  25  10  20
0   1   2   3   4   5   6
# 바로 이전으로부터 업데이트 된 값
0   0  30  35  55  65  65  
0  10  20  25  45  45  75    

dp = [[1]*2]*3
print(dp)

f(x) = max(g(x), h(x))
g(x) = h(x-1) + arr[x]
h(x) = max(g(x-2), h(x-2)) + arr[x]
     = f(x-2) + arr[x]



n = int(input())
step=[]
for _ in range (n):
    step.append(int(input()))


sum = 0
check = [False] * n
check[0] = True

jump = 1

if n == 1:
    print(1)
else:
    while (jump + 1 < n-1):
        # 연속된 계단 밟을 수 없음
        if check[jump] == True and (jump + 2) == n-1:
            break
        else:
            if (check[jump-1] == True and check[jump-2] == True):
                sum += step[jump+1]
                check[jump+1] = True
                jump = jump+1
            else:
                # 다음 계단 밟기
                one = sum + step[jump]
                # 다다음 계단 밟기
                two = sum + step[jump+1]

                #뭐가 더 큰지 확인
                if one > two:
                    sum += step[jump]
                    check[jump] = True
                    jump += 1
                else:
                    sum += step[jump+1]
                    check[jump+1] = True
                    jump += 2
    #마지막 계단 밟기
    sum += step[-1]
    print(sum)



6
123
14
3
2
13
4

답: 143
출력: 154


6
60
10
61
14
9
7
---
142

5
100
100
3
2
1
---
203

6
10
20
15
25
10
20
---
75
"""

