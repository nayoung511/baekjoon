n = int(input())
arr = [i for i in range ()]
num=[]

def solve(k):
    if len(num) == n:
        return
    
    for i in range (k, 5):
        x = [int(a) for a in str(i)]
        print(x)
        
        flag = True
        for j in range (len(x)-1):
            if x[j] < x[j+1]:
                flag = False
                break

        if flag == True:
            num.append(i)
            print(num)
            solve(k+1)
        else:
            continue

solve(0)

if n > len(num):
    print(-1)
else:
    print(num[n-1])