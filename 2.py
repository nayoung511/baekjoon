flag = True
num = 1
while (flag == True):
    a = input()
    if a == 'END':
        flag = False
        break

    big = []
    small = []
    
    a = [char for char in a]
    for i in range (len(a)-1):
        s = ""
        if a[i] == "*":
            s = s + a[i]
            while a[i+1] == ".":
                s = s + a[i+1]
                i = i+1
        if s != "":
            small.append(s)

    
    big.append(small)
    check = big[0]
    flag_check = True
    for item in big[0]:
        #print(item, check)
        if item != check[0]:
            flag_check = False
            break

    if flag_check != False:
        print(num, "EVEN")
    else:
        print(num, "NOT EVEN")
    
    num+=1

