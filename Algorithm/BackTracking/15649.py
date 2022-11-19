# N과 M (1)

n, m = map(int, input().split())
visited = [False for i in range (n+1)]
answer = []

def n_m(depth, n, m):
    # depth가 m과 같아 질 때까지 함수 재귀
    if depth == m:
        print(' '.join(map(str, answer)))

    for i in range (1, n+1):
        # 방문하지 않은 원소가 있다면
        if visited[i] == False:
            print(visited, i)
            
            visited[i] = True
            answer.append(i)
            
            print("answer", answer)
            n_m(depth+1, n, m)
            visited[i] = False
            print("방문했어요", i)
            answer.pop()

n_m(0, n, m)