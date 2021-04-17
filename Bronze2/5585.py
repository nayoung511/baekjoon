n = int(input())
n = 1000 - n
result = 0

print(n)
result += n // 500
n %= 500

print(1, n, result)
result += n // 100
n %= 100

print(2, n, result)
result += n // 50
n %= 50
print(3, n, result)

result += n // 10
n %= 10
print(4, n, result)

result += n // 5
n %= 5

print(result + n)
