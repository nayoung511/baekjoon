from operator import add

ans =[0,0]*41

def dp(j):
    if j == 0:
        ans[0] = [1,0]
        return ans[0]
    if j == 1:
        ans[1] = [0,1]
        return ans[1]
    if ans[j] != 0:
        return ans[j]
    else:
        i = dp(j-1)
        k = dp(j-2)
        ans[j] = list(map(add, i, k))
    return ans[j]


def main():
    t = int(input())
    
    for j in range (t):
        c = int(input())    
        a = dp(c)

        print(' '.join(map(str, a)))
        
main()