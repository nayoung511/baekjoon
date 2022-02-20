n = int(input())
x = [0] *(n+1)
x[0] = 1

def dp(n):
    if n == 0: return 1
    if n == 1: return 1
    if x[n] != 0: return x[n]
    else:
        val = 0
        for i in range (n):
            val += dp(i) * dp(n-i-1)
        x[n] = val
    return x[n]

print(dp(n))