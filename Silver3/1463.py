def calculate(c, count):
    print(c)
    if c - 1 > 1:
        c = c - 1
        count += 1

        if c % 3 == 0:
            c = c // 3
            count += 1
            return calculate(c, count)

        if c % 2 == 0:
            c = c // 2
            count += 1
            return calculate(c, count)

        return calculate(c, count)

    return count
    

def main():
    c = int(input())
    count = 0
    print(calculate(c, count))

main()