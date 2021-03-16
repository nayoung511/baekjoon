import re

def main():
    c = int(input())
    num = list()

    for i in range(c):
        s = input()
        #extract int
        temp = re.findall(r'\d+', s)
        res = list(map(int, temp))
        num.append(res)

    #make a flat list
    answer = [n for val in num for n in val]

    answer.sort()
    for i in range (len(answer)):
        print(answer[i])
main()