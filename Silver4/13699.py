n = int(input())
x = [0] *(10**6)

def dp(n):
    if n == 0: return 1
    if x[n] != 0: return x[n]
    else:
        val = 0
        for i in range (n):
            val += dp(i) * dp(n-i)
        x[n] = val
    return x[n]

print(dp(n))