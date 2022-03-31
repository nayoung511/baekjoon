def swap(box, i, j):
    length = (len(plain) // len(key))
    col = i
    col2 = j

    for i in range (length):
        temp = box[]
        box[i] = box[i+1]
        box[i+1] = temp



def prin(box, key):
    for i in range (len(plain) // len(key)):
        for j in range (len(key)):
            print(box[i][j], end='')
        print("\n")
key = input()
plain = input()

plain = list(plain)
box = [[0 for i in range (len(key))] for j in range (len(plain) // len(key))]


c = 0
for i in range (len(plain) // len(key)):
    for j in range (len(key)):
        box[i][j] = plain[c]
        c+=1
print(key)
prin(box, key)

key2 = list(key)
key2.sort()

for i in range (len(key)-1):
    if key2[i] > key2[i+1]:
        swap(box, i, i+1)
        prin(box, key)



