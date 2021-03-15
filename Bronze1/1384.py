def nastyP(c):
    count_p = 0
    group = list()

    answer = list()
    
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
                        str1 = group[nasty][0], "was nasty about", group[i][0] 
                        print(str1)
                        answer.append(str1)

                elif group[i][j] == 'P':
                    count_p += 1
                    if count_p == c * (c-1):
                        answer.append("Nobody was nasty")
                        #print("Nobody was nasty")

    return answer


def main():
    nGroup = 0
    result = list()

    while True:
        c = input()

        if c == '0':
            exit(1)
            break

        if c != '0':
            result.append(nGroup)
            
            print(nastyP(int(c)))
            #result[nGroup].append(nastyP(int(c)))
            
            nGroup += 1

    for i in range (nGroup):
            print(result[i])

main()