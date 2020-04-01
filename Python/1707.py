# 1707번 이분 그래프
from collections import deque
import sys, copy

# bfs
def bfs(start):
    global graph, V, visit

    q = deque()
    q.append([start,1])

    while q:
        cur, color = q.popleft()

        for neighbor in graph[cur]:
            if visit[neighbor] == 0:
                # 인접한 곳에 컬러를 변경
                visit[neighbor] = 3 - color
                q.append([neighbor, 3 - color])

# 연결된 노드인데 같은 색이 있는지 확인
def check(visit, graph):
    for i in range(V):
        for node in graph[i]:
            if visit[i] == visit[node]:
                return False
    return True

# main
T = int(input())

for _ in range(T):
    V, E = [int(x) for x in sys.stdin.readline().split()]

    graph = [[] for _ in range(V)]
    for _ in range(E):
        x, y = [int(x) for x in sys.stdin.readline().split()]
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)

    
    visit = [0 for _ in range(V)]
    for i in range(V):
        if not visit[i]:
            visit[i] = 1
            bfs(i)

    if check(visit, graph):
        print("YES")
    else:
        print("NO")
