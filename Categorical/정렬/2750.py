def main():
    n = int(input())
    lst=[]
    for i in range(n):
        r = int(input())
        lst.append(r)

    for i in range(len(lst)):
        lst.sort()

    for i in range(len(lst)):
        print(lst[i])

main()