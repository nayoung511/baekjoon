import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    print()
    # m = 격자 크기, n = 로봇의 수
    m, n = map(int, input().split())
    x_coordinates = []
    y_coordinates = []

    far_robot_x = 0
    far_robot_y = 0
    maxx = 0
    # 로봇 위치
    for _ in range (n):
        x, y = map(int, input().split())
        x_coordinates.append(x)
        y_coordinates.append(y)

        if x + y> maxx:
            maxx = x+y
            far_robot_x = x
            far_robot_y = y

    print(y_coordinates, far_robot_x, far_robot_y)
    count_instruction = 0
    # 한 줄로 정렬
    count_instruction += far_robot_x - 1
    print("after y", count_instruction)
    
    print("왼쪽 이동", max(y_coordinates), "   오른쪽 이동", m-min(y_coordinates))
    # 왼쪽 이동이 더 가깝다면
    if max(y_coordinates) - 1 < m - min(y_coordinates):
        print("here")
        count_instruction += max(y_coordinates) - 1
    else: # 오른쪽 이동이 더 가깝다면
        count_instruction += m-min(y_coordinates)

    print("#", t+1, sep='', end=' ')
    print(count_instruction)

"""
4
6 4
2 3
3 2
1 4
4 5
5 3
5 4
4 4
5 5
5 2
1 2
5 5
5 2
1 2
5 3

"""