from sys import stdin

n, s = map(int, stdin.readline().split())
num = list(map(int, stdin.readline().split()))
count = 0

def subsequence(idx, sub):
    global count
    if idx == n:
        return
    sub += num[idx]
    if (sub == s):
        count += 1
    
    subsequence(idx+1, sub)
    subsequence(idx+1, sub - num[idx])

subsequence(0,0)
print(count)

    
    