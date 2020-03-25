# 11724번 연결 요소의 개수
from collections import deque
import sys

# bfs
def bfs(n, g, start, visit):
    q = deque()
    q.append(start)

    while q:
        b_node = q.popleft()
        visit[b_node] = True

        for node in g[b_node]:
            if not visit[node]:
                visit[node] = True
                q.append(node)

    return visit

# main
n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    s, e = [int(x) for x in sys.stdin.readline().split()]
    
    # 무방향 그래프
    g[s-1].append(e-1)
    g[e-1].append(s-1)

visit = [False] * n
count = 1
for i in range(n):
    if not visit[i]:
        visit = bfs(n,g,i,visit)
        count += 1

print(count-1)
