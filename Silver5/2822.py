def main():
    score = dict()
    result = list()
    index = list()

    for i in range (1, 9):
        c = int(input())
        score[i] = c

    score = dict(sorted(score.items(), key=lambda item: item[1]))

    for k, v in score.items():
        result.append([k,v])

    sum = 0
    for i in range (3, len(result)):
        sum += result[i][1]
        index.append(result[i][0])

    index.sort()
    print(sum)
    str1 = ' '
    print(str1.join(map(str,index)))


main()