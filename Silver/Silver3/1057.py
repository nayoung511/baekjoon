n, k, l = input().split()

n = int(n)
k = int(k)
l = int(l)

count = 0

while(n):
    if ((l+1)/2 == (k+1)/2):
        break
    k = int((k + 1) / 2)
    l = int((l + 1) / 2)
    count += 1
    n = n / 2

print(count)


"""
N명의 참가자 
if 홀수? 마지막 자동 진출

1. 1라운드에서 끝나는지 검사
1,2 3,4 

2. 두 수의 차이가 1이고, l이 홀수 일 때

1 3 5 7 9 11 13 15 17 20 21... 31

"""