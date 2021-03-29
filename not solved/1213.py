from collections import Counter
def evenLetter(c):
    count = 0

    ans = []
    
    #c.sort(reverse=True)
    print(c)

    for i in range (len(c) // 2 +1):
        ans.insert(0, c[i][0])
        ans.insert(len(c)-i-1, c[i][0])

        print(ans)

    return ans
    


def oddLetter(c):
    count = 0
    c = dict(c)
    for i in range (len(c)):
        if c.values() % 2 != 0:
            count += 1
            if count > 1:
                return "I'm Sorry Hansoo"

    
def main():
    c = input()
    count = 0

    if len(c) % 2 == 0:
        d = Counter(c)
        for i in range (len(d)):
            if int(list(d.values())[i]) % 2 != 0:
                count += 1
                if count == len(c):
                    print("I'm Sorry Hansoo")
        if count != len(c):
            print(evenLetter(c))

    else:
        c = Counter(c)
        oddLetter(c)



main()