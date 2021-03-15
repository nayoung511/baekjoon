def split(a):
    return [char for char in a]

def main():
    check = [False] * 9
    goal = [True] * 9

    result = ''
    

    n = int(input())
    val = list()

    count = 2

    for j in range (n):
        num = int(input())
        val.append(num)
    flag = False
    
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