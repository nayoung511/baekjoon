s = list(input())
num = list(set(s))
print(num)
count = [0 for i in range (len(num))]

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);



for j in range (len(num)):
    for i in range (len(s)):
        if num[j] == s[i]:
            count[j] += 1

print(count)

# 똑같이 들어가 있다면
n = set(count)
if len(n) == 1:
    print(factorial(count[0]))
else:
    

