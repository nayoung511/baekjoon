def main():
    c = int(input())
    lst = list()
    date = dict()

    str1=''
    #날짜를 yyyymmdd형식으로 만든다
    for i in range (c):
        s = list(map(str, input().split()))
        lst.append(s)

        if (int(lst[i][2]) < 10):
            lst[i][2] = '0' + lst[i][2]
        if (int(lst[i][1]) < 10):
            lst[i][1] = '0' + lst[i][1]
        str1 = lst[i][3] + lst[i][2] + lst[i][1]
        date[lst[i][0]] = str1

    date = sorted(date.items(), key = lambda x:x[1])
    
    print(date[-1][0])
    print(date[0][0])
main()