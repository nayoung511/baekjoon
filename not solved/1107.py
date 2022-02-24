# 지금 보고 있는 채널: 100
import sys
input = sys.stdin.readline

n = int(input()) # 이동하려는 채널

m = int(input()) # 고장난 버튼의 갯수
num = list(map(int, input().split()))

arr = [0 for _ in range (n)]
if n == 100:
    print(0)
else:
    n = list(map(int, input().rstrip())) 
    for i in range (len(n)):
        for j in range (len(num)):
            if n[i] not in num:
                arr[i] = n[i]
            else:
        
