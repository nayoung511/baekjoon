from sys import stdin

def coloring(n, house, visited):
    minimum_cost, idx = 0,0
    print("n", n)
    
    if n == 0:
        # find the minimum value from cost
        minimum_cost = min(house[n])
        idx = house[n].index(minimum_cost)

        # check if the color is not yet taken
        # if visited[idx] == False:
        #     visited[idx] = True
        print("here", minimum_cost)
        sumOfCost[0] += minimum_cost

        # remove the house[i+1] value
        print("i'm in ", n)
        print("I will change", house[n+1][idx])
        house[n+1][idx] = 1001

    elif n < len(house)-1:
        minimum_cost = min(house[n])
        idx = house[n].index(minimum_cost)
        house[n][idx] = 1001

        # 다음 값을 구하기 위해 2nd smallest 값을 찾음 
        next_minimum = min(house[n])
        house[n][idx] = minimum_cost

        nn_mini = min(house[n+1])
        next_idx = house[n+1].index(nn_mini)
        house[n+1][next_idx] = 1001
        
        temp = min(house[n+1])
        house[n+1][next_idx] = nn_mini
        print("house", house[n], house[n+1])


        # 내가 고른 값이 미래에 고를 값보다 cost가 low한가? 
        print(minimum_cost, nn_mini, next_minimum, temp)
        print(abs(minimum_cost - nn_mini), abs(next_minimum - temp), next_minimum - minimum_cost) 
        print(abs(minimum_cost - nn_mini) > (abs(next_minimum - temp) + (next_minimum - minimum_cost)))
        if (minimum_cost - nn_mini) > (abs(next_minimum - temp) + (next_minimum - minimum_cost)):
            minimum_cost = next_minimum
            house[n+1][idx] = nn_mini
            idx = house[n].index(minimum_cost)


        print(idx)
        print("in", house[n], "select", minimum_cost)
        sumOfCost[0] += minimum_cost
        house[n+1][idx] = 1001

        print("next house", house[n+1])

    else:
        print(n)
        minimum_cost = min(house[n])
        idx = house[n].index(minimum_cost)
        sumOfCost[0] += minimum_cost
        print("here", sumOfCost)

    print(sumOfCost)
    print(house, "\n\n")

    if n < len(house)-1:
        return coloring(n+1, house, visited)

        

n = int(input())
sumOfCost = [0]
# red, green, blue
house =[0] * (n)
visited = [False] * (n)
for i in range (n):
    house[i] = list(map(int, stdin.readline().split()))

coloring(0, house, visited)
print(sumOfCost)