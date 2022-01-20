from sys import stdin

def checkOne(a):
    one = "1"
    while True:
        if int(one) % int(a) != 0:
            one = one + "1"
        else:
            break
    return len(one)

num = []

for line in stdin:
    if line=='\n':
        break
    val = checkOne(line)
    print(val)