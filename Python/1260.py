# 1260번 DFS와 BFS
import sys

# DFS
def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    
    for i in range(1,n+1):
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i)

# BFS
def bfs(v):
    visit[v] = 0
    queue = [v]

    while(queue):
        v = queue.pop(0)
        print(v, end=' ')

        for i in range(1,n+1):
            if visit[i] == 1 and graph[v][i] == 1:
                queue.append(i)
                visit[i] = 0

# main
n, m, v = [int(x) for x in sys.stdin.readline().split()]

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
# dfs에서 방문 : 1, bfs에서 방문 : 0
visit = [0 for _ in range(n+1)]

# 정점 추가
for _ in range(m):
    i, j = [int(x) for x in sys.stdin.readline().split()]
    graph[i][j] = 1
    graph[j][i] = 1

dfs(v)
print()
bfs(v)