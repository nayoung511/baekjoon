from collections import deque
N = int(input())
q = deque(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
total = 9
if N <= 9 : 
  print(q[N])
  exit(0)
  
while q:
    c = q.popleft()
    for i in range(0, 10):
        if int(c[-1]) <= i : break
        q.append(c+str(i))
        total += 1
        if total == N: 
            print(q[-1])
            exit(0)

print(-1)



# import sys
# sys.setrecursionlimit(10**9)

# n = int(input())
# arr = [i for i in range (10)]
# # 0: 0번째

# start = 1

# if n >= 1023:
#     print(-1)
# elif n < 10:
#     print(arr[n])
# else:
#     cnt = 10
#     while True:
#         flag = False
#         num = list(map(int, str(cnt)))
#         for j in range (len(num)-1):
#             if num[j] <= num[j+1]:
#                 flag = True
#                 break

#         if flag == False:
#             arr.append(cnt)

#         if len(arr) == n+1:
#             print(arr[n])
#             exit()

#         cnt+=1


# # if n < 10:
# #     print(arr[n])
# # else:
# #     decreasing(0)
# #     if len(arr) < n:
# #         print(-1)
# #     else:
# #         print(arr[n])
# # # 0 1 2 3 4 5 6 7 8 9 (9)
# # # 10 20 21 30 31 32 40 41 42 
