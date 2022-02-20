"""
from math import gcd

def lcm(x, y):
    return int(x * y // gcd(x,y))

def main():
    al = list(map(int, input().split(' ')))
    lc = list()

    #1. 리스트를 sort한다.
    al.sort()

    #2. 제일 작은 수 al[0]을 제외한 4개의 수를 가지고 2개씩 최소 공배수를 찾는다.
    for i in range(1, 4):
        for j in range(i+1, 5):
            v = lcm(al[i], al[j])
            lc.append(v)

    #3. sort한다
    lc.sort()
    #print(lc)

    #4. 제일 작은 결과값과 al[0]을 lcm하여 최소공배수 값을 구한다.
    min = lcm(al[0], lc[0])
    for i in range (len(lc)):
        if(int(lcm(al[0], lc[i])) < min):
            min = lcm(al[0], lc[i])
    
    print(min)

main()

"""

def main():
    al = list(map(int, input().split(' ')))
    
    count = 0
    x = 1

    while(True):
        for i in range (5):
            if(x % al[i] == 0):
                count+=1
        
        if (count >= 3):
            print(x)
            break

        count = 0
        x += 1

main()
