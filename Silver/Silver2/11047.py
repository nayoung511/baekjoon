n, k = map(int, input().split())
coin = [0] * (n)

for i in range (n):
    coin[i] = int(input())

coin.reverse()

count = 0
val = 0
while k > 0 :
    for i in range (n):
        print("coin", coin[i])
        if coin[i] <= k:
            val = (k // coin[i])
            print("here", coin[i], val)
            count += val

            k = k - coin[i] * val
        print(k)


print(count)