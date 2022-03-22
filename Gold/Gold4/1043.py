import sys
input = sys.stdin.readline



# 사람의 수 n, 파티의 수 m 
n, m = map(int, input().split())

# 사람 체크
visited = [False for i in range(n)]
parties = [False for i in range (m)]

# 진실을 아는 사람의 수와 번호
truth = list(map(int, input().split()))

# 각 파티마다 오늘 사람의 수와 번호
party = []
for _ in range (m):
    a = list(map(int, input().split()))
    party.append(a[1:])

def checkTruth(person):
    num = []
    for i in range (m):
        if person in party[i]:
            parties[i] = True
            visited[person-1] = True
            num+=party[i]

            print("num", num)
        
    return num

# 과장된 이야기를 할 수 있는 파티의 개수
if truth[0] == 0:
    print(m)
else:
    truth = truth[1:]
    count = 0

    # 진실을 아는 사람이 없을 때까지
    while len(truth) > 0:
        for person in truth:
            print(person, visited, truth)
            if visited[person-1] == False:
                truth += (checkTruth(person))
                visited[person-1] = True
            else:
                truth.remove(person)
        

    print(visited)

    for i in range (m):
        if parties[i] == True:
            count+=1
    print(parties)
    print(m-count)
