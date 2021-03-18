def main():
    c = int(input())
    s = []

    for i in range(c):
        age, name = list(map(str, input().split()))
        s.append([int(age), name])


    s = sorted(s, key = lambda x:x[0])
    for i in s:
        print(i[0], i[1])
main()
