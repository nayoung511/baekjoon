n, m = map(int, input().split())

line = []
for _ in range (n):
    num = int(input())
    x = [int(a) for a in str(num)]
    line.append(x)


print(line)
a = 0
diff = 0
#가장 멀리 있는 같은 수를 찾음
for i in range (n):
    key = line[i][a]

    for j in range (m-1, 0, -1):
        #check right
        print("here", key, line[i][j])
        if key == line[i][j]:
            print(key, line[i][j])



            #check bottom

            # if key == line[i+j][j]:
            # #check bottom-left
            #     if key == line[i+j][a]:
            #         flag = True
            #         break


print(a)

    




