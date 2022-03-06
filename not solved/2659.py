import sys

input = sys.stdin.readline

num = list(map(int, input().split()))

start = min(num)
startIdx = 0
# find the index

for i in range (len(num)):
    if start == num[i]:
        startIdx = i
        break


smallestNum = [start for i in range (len(num))]
smallestNum = [str(int) for int in smallestNum]
smallestNum = "".join(smallestNum)
smallestNum = int(smallestNum)
#print(smallestNum, startIdx)

sipja = num[i:] + num[:i]
sipja = [str(int) for int in sipja]
sipja = "".join(sipja)
sipja = int(sipja)

print(sipja - smallestNum -1)

