n = int(input())
count = 0
#5의 배수

while (n > 0):
    if n % 5 == 0 and n!= 1:
        count += n // 5
        n = 0

    elif n > 5:
        n -= 2
        count += 1

        if n % 5 == 0 and n != 0:
            count += n // 5
            n = n - (5 * count)
            break

        if n < 0:
            count = -1

    elif n >1 and n < 5:
        if n % 2 == 0:
            count += n // 2
            break
        else:
            count = -1
            break

    else:
        count = -1
        break

print(count)