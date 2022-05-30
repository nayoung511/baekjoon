n, m = map(int, input().split())

vowel = ['a', 'e', 'i', 'o', 'u']

alpha = list(map(str, input().split()))
alpha.sort()
password = []

def solve(k):
    # n개까지 왔을 때 
    if k == n:
        count = 0
        # 최소 한 개의 모음, 최소 두 개의 자음
        for v in range (len(vowel)):
            if vowel[v] in password:
                count+=1

        if count + 2 <= n and count >= 1:
            print(*password, sep='')
            return

    for i in range (k, m):
        if alpha[i] not in password:
            if len(password) > 0:
                if alpha[i] > password[-1]:
                    password.append(alpha[i])
                    solve(k+1)
                    password.pop()
            else: # password가 비었을 때를 위해
                password.append(alpha[i])
                solve(k+1)
                password.pop()


solve(0)