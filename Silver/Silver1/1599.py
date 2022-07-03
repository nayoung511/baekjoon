n = int(input())

words = []
alpha = ['a', 'b', 'k', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'ng', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y']

def calWeight(word):
    weight = []
    for i in range (len(word)):
        for j in range (len(alpha)):
            if word[i] == alpha[j]:
                weight.append(j+1)

    return weight

values = dict()
for i in range (n):
    words.append(list(input()))

    for j in range (len(words[i])-1):
        if words[i][j] == 'n' and words[i][j+1] == 'g':
            words[i][j] = 'ng'
            words[i][j+1] = ''

    values[i] = calWeight(words[i])

sorted_keys = sorted(values, key=values.get)
for i in range (n):
    print(''.join(words[sorted_keys[i]]))
