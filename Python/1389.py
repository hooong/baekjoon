# 1389번 케빈 베이컨의 6단계 법칙
import sys

# dfs
def dfs(visit, start, cur, count):
    global steps, social, N

    visit[start] = True
    steps[start][cur] = min(steps[start][cur], count)

    for node in social[cur]:
        if not visit[node]:
            visit[node] = True
            dfs(visit, start, node, count+1)
            visit[node] = False

    visit[start] = False

# main
N, M = [int(x) for x in sys.stdin.readline().split()]

# 관계 그래프 (무방향)
social = [[] for _ in range(N)]
for _ in range(M):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    social[a-1].append(b-1)
    social[b-1].append(a-1)

# 각 관계의 최소 거리
steps = [[100 for _ in range(N)] for _ in range(N)]

# 방문 여부 저장
visit = [False for _ in range(N)]
for i in range(N):
    dfs(visit, i, i, 0)

# 케빈 베이컨 수
minStep = float('inf')
victory = 0
for i in range(N):
    kebin = sum(steps[i])
    if minStep > kebin:
        minStep = kebin
        victory = i+1
    
print(victory)
