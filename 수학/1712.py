def main():
    a, b, c = input().split()

    a = int(a)
    b = int(b)
    c = int(c)

    #a + (b * N) < c * N
    # a < n(c-b)
    #if right side is negative, then return -1 else return n

    if(c-b > 0):
        print(int((a /(c-b))+1))
    else:
        print(-1)


main()