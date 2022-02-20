n = input()
m = input()

missing = 0
if m in n:
    n1 = n.replace(m,"")

    missing = len(n) - len(n1)
    missing = missing / len(m)
print(int(missing))