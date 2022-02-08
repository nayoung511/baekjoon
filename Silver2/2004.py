def fiveMul(n):
    count = 0

    while(n >= 5):
        count += n // 5
        n = n // 5

    return count


def twoMul(n):
    count = 0

    while(n >= 2):
        count += n // 2
        n = n // 2

    return count


n, m = map(int, input().split())

count5 = fiveMul(n) - fiveMul(n-m) - fiveMul(m)
count2 = twoMul(n) - twoMul(n-m) - twoMul(m)

print(min(count5, count2))
