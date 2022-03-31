from collections import Counter

n, score, p= input().split()
n = int(n)
score = int(score)
p = int(p)

a = list(map(int, input().split()))
idx = 1
flag = True

for i in range (len(a)):
    if score >= a[i]:
        if p > n:
            a.insert(i, score)
            print("a: ", a)
            idx = i
            break
        if p == n:
            if i == len(a) - 1 and score == a[i]:
                print("here")
                flag = False
                break
            else:
                print("here")
                a.insert(i, score)
                idx = i
                break
    else:
        if p > n and i == len(a)-1:
            a.insert(len(a), score)
            idx = len(a)-1
            break

print(a)
a.sort()
c = a[:idx]
b = Counter(c)

print(b)

if flag == False:
    print(-1)
else:
    print(sum(b.values())+1)





