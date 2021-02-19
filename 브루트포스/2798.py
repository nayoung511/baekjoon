def main():
    n, m = input().split()
    n = int(n)
    m = int(m)

    #put elements inside list
    lst = list(map(int, input().split()))


    #check if the sum of elements are > m
    rst = []

    sum = 0
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if(sum + lst[k] < m):
                    #print(lst[i], lst[j], lst[k])
                    sum = lst[i] + lst[j] + lst[k]
                    #print(sum)
                    if(sum <= m):
                        rst.append(sum)
                        sum = 0
                    else:
                        sum = 0

    #print(rst)

  #print the smallest differences
    min = rst[0]
    for i in range(0, len(rst)):
        if(rst[i] > min):
            min = rst[i]
        

    print(min)


main()