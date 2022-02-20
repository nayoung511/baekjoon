from sys import stdin

# def checkSame(i, start, end):
#     start, end = 0, m-1
#     while end != start:
#         #print(i, end, start)
#         if arr[i][start] != arr[i][end]:
#             end -= 1

#         if start == end:
#             #print("same!")
#             start += 1
#             end = m-1

#         if arr[i][start] == arr[i][end]:
#             # print("    ", arr[i][start], arr[i][end])
#             # print("///", i, end, start)
#             diff = end - start
#             if (checkSpace(i, start, end, diff)) == False:
#                 end -= 1
#             else:
#                 break

#     return size



# #위에서 구한 거리만큼 나머지 꼭짓점이 떨어져 있는지 확인 
# def checkSpace(i, start, end, diff):
#     #print("hello", i+diff)
#     if (i+diff) < n:
#         #print("difffff", arr[i+diff][start], arr[i+diff][end])
#         if arr[i][start] == arr[i+diff][start]:
#             if arr[i+diff][start] == arr[i+diff][end]:
#                 size.append( (diff + 1) * (diff+1))
#                 return

#     return False
        

n, m = map(int, input().split())
arr = [0] * n
diff, start= 0,0
for i in range (n):
    arr[i] = list(map(int, stdin.readline().rstrip('\n')))

for i in range (n-1):
    for j in range (m-1):
        start = arr[i][j]

        c = min(n-i, m-j) - 1
        # 가장 큰 정사각형부터 
        while c > diff:
            if start == arr[i+c][j] and start == arr[i][j+c] and arr[i+c][j+c] == start:
                diff = c

            c -= 1
print((diff +1) * (diff +1))






#     checkSame(i, 0, n-1)

# print(max(size))