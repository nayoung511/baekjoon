n, l = map(int, input().split())

coord = []
maxx = 0
for i in range (n):
    start, end = map(int, input().split())
    coord.append((start, end))
coord.sort()

current_coordiante = coord[0][0]
count_log = 0

for i in range (n):
    # 다음 물웅덩이의 시작점이 현재 coordinate 보다 멀다면
    # 이동시켜줌
    if coord[i][0] > current_coordiante:
        current_coordiante = coord[i][0]

    # 시작점

    while coord[i][1] > current_coordiante:
        #print("amount", l * (((coord[i][1] - current_coordiante) // l) + 1))
        count_log += 1
        current_coordiante += l

print(count_log)