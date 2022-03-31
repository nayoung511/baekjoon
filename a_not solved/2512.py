n = int(input())
budget = list(map(int, input().split()))
m = int(input())

budget.sort()
start, end = 0, 1
sumOfBudget = 0

if sum(budget) < m:
    print(max(budget))

else:
    while (start <= end):
        if sumOfBudget <= m:
            check = budget[start]
            if start != 0:
                sumOfBudget += sum(budget[0:start])


            sumOfBudget += budget[start] - budget[end]
            end += 1
        else:
            start

"""
110, 120, 140, 150

110) 110, 110, 110, 110   = 420

--->
120) 110, 120, 120, 120   = 470
140) 110, 120, 140, 140   = 510


"""