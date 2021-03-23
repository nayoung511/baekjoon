def main():
    s = input()
    a = list(s)
    count = 10

    #consecutive cases e.g) 1,2,3,4 
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            result = a[i+1]

        elif a[i] == a[i+1] or a[i] > a[i+1]:
            #10의 자리를 붙여준다
            if a[i+1] + count > a[i]:
                a[i+1] = a[i+1] + count
                if a[i+1] < result:
                    result = a[i+1]
                
            elif a[i] > a[i+1] + count:
                #숫자 뒤에 0을 붙여본다
                if a[i+1] * 10 > a[i]:
                    a[i+1] = a[i+1] * 10
                    if a[i+1] < result:
                        result = a[i+1]

                #십의 자리를 올린다
                else:
                    count += 10
                    a[i+1] = a[i+1] + count
                    if a[i+1] < result:
                        result = a[i+1]


            

    
    print(result)



main()