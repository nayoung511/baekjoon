

def fibonacci(n, c0, c1):
    if n == 0:
        c0 += 1
        print("c0:", c0)
        return 0, c0, c1
    elif n == 1:
        c1 += 1
        print("c1", c1)
        return 1, c0, c1
    else:
        print("combine", c0, c1)
        return fibonacci(n-1, c0, c1) + fibonacci(n-2, c0, c1)
        #return c0, c1

def main():
    t = int(input())

    for j in range (t):
        c0 = 0
        c1 = 0

        c = int(input())
        d = list(fibonacci(c, c0, c1))

        d = [d[i:i+3] for i in range(0, len(d),3)]

        

        print(d)

main()


