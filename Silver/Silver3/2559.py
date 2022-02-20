n, k = map(int, input().split())
temp = list(map(int, input().split()))

# calculate sum(temp[0:k])
val = sum(temp[0:k])
#print(val)
max = val

start, end = 0, k

# start값을 빼주고 end값을 더해주는 식
for _ in range(0, len(temp) - k):
    val = val - temp[start] + temp[end]
    #print(temp[(start+1):(end+1)], val)

    if val > max:
        max = val
    start += 1
    end += 1

    if start == k and end != len(temp) -1:
        val = sum(temp[start:end])
        #print("new val:", val)

print(max)
    