def main():
    n = int(input())
    count = 0   #count가 짝수면 cy, count가 홀수면 sk

    while n > 0:
        if n >= 3:
            n -= 3
            count += 1
            if n == 0:
                break

        elif n >= 1 and n < 3:
            n -= 1
            count += 1
            if n == 0:
                break

    if count % 2 == 0:
        print("CY")
    else:
        print("SK")
main()