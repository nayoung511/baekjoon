def check (a, b):
    if 1 in a:
        idx = a.index(1)
        for i in range (len(a)):
            if a[idx] == b[idx]:
                return True
    else:
        return False


flag = True
while (flag == True):
    a = int(input())
    if a == 0:
        flag = False
        break
    con = list(map(str, input().split()))
    value = []

    matrix = [[0 for i in range (a)] for j in range (a)]

    for i in range (a - 1):
        small_con = input().split(" = ")
        for j in range (a):
            if small_con[0] == con[j]:
                matrix[i][j] = 1
                break
        data = small_con[1].split()
        idx = con.index(data[1])
        matrix[i][idx] = int(data[0])

    for i in range (a-1, 0, -1):
        #find the non 1 and non 0 value
        max_initial = max(matrix[i-1])
        for j in range (a):
            d = matrix[i][j]
            if 0 in matrix[0]:

                if check (matrix[i], matrix[i-1]) == True:
                    for k in range (a):
                        matrix[i-1] = [int(matrix[i][k]) + int(matrix[i-1][k]) for k in range(len(matrix[i]))]
    
                else:
                    if d != 0 and d != 1:
                        idx_max = matrix[i-1].index(max_initial)
                        if idx_max == j:
                            matrix[i-1][matrix[i].index(1)] = max_initial // d
                        else:# max_initial >= d:
                            matrix[i-1][j] = max_initial * d
            else:
                break


    for i in range (a):
        if matrix[0][i] == 2:
            matrix[0][i] = 1
        matrix[0][i] = str(matrix[0][i]) + con[i]

    matrix[0].sort(reverse=True)

    for i in range (a-1):
        print(matrix[0][i], end= ' = ')

    print(matrix[0][-1])

