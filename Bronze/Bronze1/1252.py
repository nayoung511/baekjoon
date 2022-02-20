
def btod(a):
    s = str(a)
    s = list(s)

    val = 0
    for i in range(len(s)):
        val += int(s[len(s)-i-1]) * pow(2, i)
    return val

def dtob(a):
    val = list()
    while(a != 1):
        if (a % 2 == 1):
            val.append(1)
            a = int(a/2)
        elif (a % 2 == 0):
            val.append(0)
            a = int(a/2)
    
    # 2/2 = 1
    val.append(1)
    val.reverse()
    return val


def main():

    a,b= input().split()

    a=int('0b'+a,2)
    b=int('0b'+b,2)
    
    c= format(a+b,'b')
    print(c)


"""
   
   
    n, m = input().split()


    sum = bin(int(n,2) + int(m,2))
    print(sum[2:])

    n = int(n)
    m = int(m)

    if (n == 0 and m == 0):
        print(0)

    else:
        n = btod(n)
        m = btod(m)

        result = dtob(n + m)
        
        print(''.join(str(e) for e in result))
"""

main()
