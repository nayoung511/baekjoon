import sys
input = sys.stdin.readline

n = int(input()) # 크레인의 수
weight = list(map(int, input().split())) # 각 크레인이 들 수 있는 무게
m = int(input())
cargo = list(map(int, input().split())) # 화물의 크기
visited = [0 for i in range (m)]
ideal = [1 for i in range (m)]

# 정렬
weight.sort(reverse=True)
cargo.sort(reverse=True)

minute = 1 # 몇 분 걸리는지
idx = 0 # 몇 번째 화물인지
num = 0 # 몇 번째 크레인인지
# 크레인이 들 수 있는 무게보다 더 무거운 화물이 있다면 -1
if max(cargo) > max(weight):
    print(-1)
    
else:
    while num != m:
        print(idx, num)
        if weight[idx] >= cargo[num]:
            # 다음 크레인에 싣기
            idx += 1
            # 다음 화물로 이동
            visited[num] = 1
            num += 1

            # 모든 크레인이 사용 중이라면
            if idx >= n:
                # 다시 처음으로 초기화
                idx = 0
                minute += 1
            

        # 현재 크레인에 현재 화물을 실을 수 없다면
        else:
            # 다음 화물 체크
            num += 1

            if num >= m-1:
                num = 0


print(minute)