import sys
input = sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
sorted_arr=list(sorted(set(arr)))

dic = {value: index for index, value in enumerate(sorted_arr)}

for i in arr:
    print(dic[i], end=' ')