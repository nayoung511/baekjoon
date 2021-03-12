def checkF(a, b):
    count = 0
    for i in range (len(b)):
        if (a == b[i]):
            count += 1

    return count

def main():
    s = str(input()).upper()
    s = list(s)
    dc = dict()

    if(len(s) == 1):
        print(s[0])

    else:
        for i in range (len(s)):
            if s[i] not in dc:
                key = s[i]
                count = checkF(key, s)
                dc[key] = count 

        #value들만 비교
        sort_dc = sorted(dc.items(), key = lambda x: x[1], reverse=True)
        max = sort_dc[0][1]

        if (sort_dc[1][1] == max):
            print("?")
        else:
            print(sort_dc[0][0])

main()