def split(a):
    return [char for char in a]

def main():
    check = [False] * 10
    goal = [True] * 10

    result = ''
    
    n = int(input())
    val = list()

    count = 2

    for j in range (n):
        num = int(input())
        val.append(num)

    for k in range(len(val)):
        count = 2
        start = val[k]

        if val[k] == 0:
            result = "INSOMNIA"
 
        else:
            check = [False] * 10
            goal = [True] * 10
            flag = False

            while(flag == False):
                sliced_val = split(str(val[k]))
                #print(sliced_val)
                for i in range(len(sliced_val)):
                    idx = int(sliced_val[i])
                    if (check[idx] == False):
                        check[idx] = True

                        if check == goal:
                            flag = True
                        #print(check)
                
                if flag == True:
                    break

                val[k] = start * count
                count += 1
                    
        answer = val[k]
        mesPrint = "Case #" + str(k+1) + ":"
        if answer == 0:
            print(mesPrint, result)

        else:
            print(mesPrint, answer)

main()

"""
Case #1: INSOMNIA
Case #2: 10
Case #3: 90
Case #4: 110
Case #5: 5076

"""
"""
    for i in range (n):
        if val[i] == 0:
            result = 'INSOMNIA'
            break

        while(flag != True):
            d = val[i]
            data = split(str(d))
            print(data)

            for j in range (len(data)):
                if check[int(data[j])] == False:
                    check[int(data[j])] = True

                if check == goal:
                    result = str(val[i])
                    flag = True
                    break
               
            d = d * count
            count += 1

    answer = "Case #" + str(n) + ":"
    print(answer, result)

main()
"""