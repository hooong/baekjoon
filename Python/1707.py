# 1707번 이분 그래프
from collections import deque
import sys

# bfs
def bfs(start):
    global graph, visit

    q = deque([start])
    while q:
        v = q.popleft()

        for neighbor in graph[v]:
            if not visit[neighbor]:
                visit[neighbor] = True
                q.append(neighbor)

# main
T = int(input())

for _ in range(T):
    V, E = [int(x) for x in sys.stdin.readline().split()]

    graph = [[] for _ in range(V)]
    for _ in range(E):
        x, y = [int(x) for x in sys.stdin.readline().split()]
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)

    visit = [False for _ in range(V)]
    count = 0
    for i in range(V):
        if not visit[i]:
            visit[i] = True
            count += 1
            bfs(i)
    
    if count == 2:
        print("YES")
    else:
        print("NO")