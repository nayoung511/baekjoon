from sys import stdin

def checkSame(i, start, end):
    start, end = 0, m-1
    while end != start:
        #print(i, end, start)
        if arr[i][start] != arr[i][end]:
            end -= 1

        if start == end:
            #print("same!")
            start += 1
            end = m-1

        if arr[i][start] == arr[i][end]:
            #print("    ", arr[i][start], arr[i][end])
            #print("///", i, end, start)
            diff = end - start
            checkSpace(i, start, end, diff)
            break

    return size



#위에서 구한 거리만큼 나머지 꼭짓점이 떨어져 있는지 확인 
def checkSpace(i, start, end, diff):
    #print("hello", i+diff)
    if (i+diff) < n:
        #print("difffff", arr[i+diff][start], arr[i+diff][end])
        if arr[i+diff][start] == arr[i+diff][end]:
            #print("here")
            
            size.append( (diff + 1) * (diff+1))

    return 0
        

n, m = map(int, input().split())
arr = [0] * n
max_size = 1
size = [1]
for i in range (n):
    arr[i] = list(map(int, stdin.readline().rstrip('\n')))

#print(arr)

for i in range (n-1):
    #print(size)
    checkSame(i, 0, n-1)
    #print(size)
    #print(size, max_size)


print(max(size))