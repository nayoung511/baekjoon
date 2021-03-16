def split(a):
    return [char for char in a]

def main():
    alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 
    'six', 'seven', 'eight', 'nine']

    m, n = input().split()
    m = int(m)
    n = int(n)

    wlist = list()
    answer = list()

    for i in range (m, n+1):
        c = split(str(i))

        word = ''
        for j in range (len(c)):
            w = alpha[int(c[j])]
            if j != len(c)-1:
                w = w +' '
            word += w
            #print(word)

        wlist.append(word)
    wlist.sort()

    #convert to int
    for i in range(len(wlist)):
        c = wlist[i].split()
        integer = ''
        for j in range(len(c)):
            
            for k in range(len(alpha)):
                if c[j] == alpha[k]:
                    integer += str(k)
        answer.append(integer)
    
    count = 0
    for i in range(len(answer)):
        if count == 10:
            print()
            count = 0
        if i == len(answer)-1:
            print(answer[i])
        else:
            print(answer[i],end = ' ')
            count += 1
main()