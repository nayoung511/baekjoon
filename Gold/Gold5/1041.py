n = int(input())
# A, B, C, D, E, F
num = list(map(int, input().split()))

# 하나의 주사위만 주어졌을 때,
if n == 1:
    # 주사위 값을 다 더해 Max를 빼준다
    print(sum(num) - max(num))
else:
    # 면 1, 2, 3개 
    side1, side2, side3 = 0, 0, 0

    side1 = min(num)

    # 만날 수 없는 짝
    # A - F
    # D - C
    # E - B

    side2 = min(
        num[0]+num[1],
        num[0]+num[2],
        num[0]+num[3],
        num[0]+num[4],
        num[1]+num[2],
        num[1]+num[3],
        num[1]+num[5],
        num[2]+num[4],
        num[2]+num[5],
        num[3]+num[4],
        num[3]+num[5],
        num[4]+num[5]
    )

    side3 = min(
        num[0]+num[1]+num[2],
        num[0]+num[1]+num[3],
        num[0]+num[3]+num[4],
        num[0]+num[2]+num[4],
        num[1]+num[2]+num[5],
        num[1]+num[3]+num[5], 
        num[2]+num[4]+num[5], 
        num[3]+num[4]+num[5]
    )

    summ = side1 * ((n-2) * (n-2) + (n-1)*(n-2) * 4)
    summ += side2 * ((n-2) * 4 + (n-1) * 4)
    summ += side3 * 4

    print(summ)