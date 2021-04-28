def main():
    n = int(input())
    s = [0] * (n+1)
    s[0] = 0
    
    for i in range (n):
        s[i] = (int(input()))
    sum = s[n-1]
    #연속된 2개 이상의 계단 x
    if n == 1: 
        return s[1]
    if n == 2: 
        return s[1] + s[2]
    else:
        for i in range (n // 2 + 1, -2, -2):
            print(i, s[i], s[i-1])
            sum += max(s[i], s[i-1])
            print(sum)
    
    print(sum)

main()

