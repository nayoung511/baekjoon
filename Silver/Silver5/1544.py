def checkSame(a, b, c):
    #a = word
    #b = index
    #c = word (a 와 같은지 비교)
    #print(a, c)
    a = a[b:] + a[:b]
    
    if a == c:
        return True
    else:
        return False

def main():
    c = int(input())

    w = list()
    fin = list()
    count = 1

    for i in range (c):
        s = list(map(str, input().split()))
        w.append(s)

    word = [n for val in w for n in val]

    #미리 먼저 첫번째 단어를 넣어준다 
    fin.append(word[0])

    for i in range (1, c):
        s = word[i]
        flag = False
        #print(fin)
        #fin 배열에 저장된 단어들과 길이가 같은지 확인
        for j in range (len(fin)):
            #print(s, fin[j])
            if len(s) == len(fin[j]):
                #같은 시작점을 찾는다
                for k in range (len(s)):
                    if s[k] == fin[j][0]:
                        #시작점을 시작으로 fin 배열에 저장된 단어와 같은지 확인
                        flag = checkSame(s, k, fin[j])
                        if flag == True:
                            break
                if flag == True:
                    break

        #fin 배열에 저장된 단어들과 길이가 같은게 없다면
        if flag == False:
            count += 1
            #print("flag", count)
            fin.append(s)
            
                        
    print(count)


main()