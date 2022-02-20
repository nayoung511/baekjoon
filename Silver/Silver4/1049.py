def main():
    n, m = input().split()

    n = int(n)  #끊어진 기타줄
    m = int(m)  #기타줄 브랜드

    package = []        
    unit = []

    for i in range (m):
        a, b = input().split()
        a = int(a)
        b = int(b)

        package.append(a)
        unit.append(b)

    package.sort()
    unit.sort()
    

    min_package = package[0]
    min_unit = unit[0]

    if n < 6:
        if n * min_unit < min_package:
            sum = n * min_unit
        else:
            sum = min_package

    else:
        sum = min_package * (n // 6)
        sum += (n - (6 * (n // 6))) * min_unit

        if ((n // 6) + 1) * min_package < sum:
            sum = ((n // 6) + 1) * min_package

        if (n * min_unit) < sum:
            sum = n * min_unit

    print(sum)


main()