import math

def main():
    n, m = input().split()

    n = int(n)  # 소시지 수
    m = int(m)  # 평론가 수

    count = 0  # 커팅 횟수 
    if n % m != 0:
        count = 1   

    if n > m:
        n = n-m

    #한 평론가에게 줄 소시지 양
    p = n/m
    p, s = math.modf(p)

    p = round(p, 2)

    
    remainder = 1 - p
    #print(remainder)

    rem = round(remainder,2)



    s = n - p
    s = round(s, 2)
















    """


    while(s > 0):
        print(p)
        print("remaining sausage", rem)

        if rem < p and  rem != 0.01:
            #print(p, rem)
            need = abs(p - rem)
            need = round(n, 2)
            print("you need", need)

            print("we have", s, "sausage now")
            s = s - need - rem
            s = round(s, 2)
            print("we cut. Now we have", s, "sausage")
            
            
            rem, whole  = math.modf(s)
            rem = round(rem,2)
            rem = abs(rem)
            print(rem)
            
            count+=1

            print("we cut", count, "times")

        elif rem > p:
            rem = rem - p
            rem = round(rem,2)
            print("after cutting sausage", rem)
            
            count+= 1

        elif rem == p or rem - p == 0.01:
            print("it's same so no cut")
            s = s - rem
            break

        elif rem == 0.01:
            print("remainder is same as 0.01")
            rem = round(remainder, 2)
            print("new remainder after cutting", rem)
            if s == 0:
                break
            
        
        
        if round(remainder,2) != p:
            # 새로운 소세지에서 자른다 
            if round(remainder,2) > p:
                print("bigger")
                remainder -= p
                remainder= round(remainder,2)
                print(round(remainder, 2))
                count += 1

            else:
                print("smaller")
                count += 1
                n -= 1
                remainder = p - remainder
                remainder = round(remainder,2)

            if remainder == 0.01:
                break
        """

    print(count)
    

main()