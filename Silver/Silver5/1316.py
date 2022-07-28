import sys
input = sys.stdin.readline

n = int(input())
count = 0
words = []

# 이전에 등장했던 char이 또 등장하면 안된다
for i in range (n):
    words.append(list(input().rstrip()))

def checkGroupWord(word):
    groupWord = True

    for i in range (len(word)-1):
        if word[i+1] != word[i]:
            newWord = word[i+1:]

            if newWord.count(word[i]) > 0:
                groupWord = False
    return groupWord


for i in range (n):
    if checkGroupWord(words[i]) == True:
        count += 1

print(count)