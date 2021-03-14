def nastyP(c):
    count_p = 0
    group = list()
    
    for i in range (c):
            children = list(map(str, input().split()))
            group.append(children)
    
    for i in range (0, c):
            for j in range (1, c):
                if group[i][j] == 'N':
                    #remember the index
                    if i < j:
                        ia = i+c
                        nasty = ia - j
                    else:
                        nasty = i - j
                    print(group[nasty][0], "was nasty about", group[i][0])

                elif group[i][j] == 'P':
                    count_p += 1
                    if count_p == c * (c-1):
                        print("Nobody was nasty")

def main():
    nGroup = 0
    while True:
        c = input()

        if c == '0':
            break

        if c != '0':
            nGroup += 1

            print("\nGroup", nGroup)
            nastyP(int(c))

main()