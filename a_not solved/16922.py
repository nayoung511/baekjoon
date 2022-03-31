n = int(input())
num = [1, 5, 10, 50]
visited = [False] * (5)   # 0 == not yet, 1 == visited
rs=[]

def chess(m):
    if m == 4:
        print(rs)
        return
    for i in range (n+1):
        #rs.append(num[i])
        if visited[m-1] == False:
            visited[m-1] = True
            rs.append(num[m-1])
            print(i, visited)
            print(rs)
            chess(m+1)
            # visited[i] = False
            # rs.pop()

chess(0)





