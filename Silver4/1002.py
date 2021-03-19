import math

def solve(d, r1, r2):
    if (r1 + r2 < d):
        return (0)
    elif (abs(r1 - r2) > d):
        return(0)
    elif (d == 0 and r1 == r2):
        return(-1)
    elif r1 + r2 == d:
        return(1)
    elif abs(r1-r2) == d:
        return(1)
    else:
        return(2)

def main():
    c = int(input())
    a = []

    for i in range (c):

        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        d = math.sqrt((pow((x1-x2), 2) + pow((y1- y2),2)))
        a.append(solve(d, r1, r2))

    for i in range (c):
        print(a[i])

        


main()