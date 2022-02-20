def main():
    n = int(input())

    ns = list()

    for i in range (n):
        value = list(map(int, input().split()))
        ns.append(value)

    #print(ns)
    
    countL = [0] * n
    #print(countL)

    for i in range (n):
        #print("row", i)
        visited = [False] * n
        for j in range (n):
            
            
            key = ns[j][i]
            for k in range(j+1, n):
                #print(key, ns[k][i])


                if (key == ns[k][i]):
                    #print("key", key, "and ", ns[k][i], " are same")
                    #print(visited)
                    if(visited[k] != True):
                        if(visited[j] != True):
                            countL[k] += 1
                            countL[j] += 1
                            visited[k] = True
                            visited[j] = True
                            #print(visited)
                            #print(countL)
                        else:
                            countL[k] += 1
                            visited[k] = True
                            #print(visited)
                            #print(countL)
            #print("--------------------------------------------")

        #print(countL)
        #print(visited)

   # print("--------------------------------------------")
    
    #print(countL)
                
    max = 0

    for i in range(len(countL)):
        if countL[i] > max:
            max = countL[i]

    print(max+1)


main()