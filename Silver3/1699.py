n = int(input())
x = [0] * (n+1)

def dp(n):
    if n == 1: return 1
    if n == 2: return 4
    if n == 3: return 9
    if x[n] != 0: return x[n]
    else:
        

