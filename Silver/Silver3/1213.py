## 다시 풀어야 됨

s = input()

slist = list(map(str, s))
slist.sort()

arr = ['' for _ in range (len(slist))]
print(arr)
a_set = set(slist)
dict = {}
for i in range (len(a_set)):
    if 
