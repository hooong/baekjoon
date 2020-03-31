# 2644번 촌수계산
from collections import deque
import sys

# bfs
def bfs(g, start, end, n, m):
    q = deque()
    q.append([start,0])

    visit = [False for _ in range(n)]
    visit[start] = True
    
    while q:
        p, count = q.popleft()

        for family in g[p]:
            # p2로 도착
            if family == end:
                return count+1

            if not visit[family]:
                visit[family] = True
                q.append([family,count+1])
    return -1   # 갈 수 있는 경로가 없음

# main
n = int(input())
p1, p2 = [int(x) for x in sys.stdin.readline().split()]
m = int(input())

# 무방향그래프
g = [[] for _ in range(n)]
for _ in range(m):
    x, y = [int(x) for x in sys.stdin.readline().split()]
    g[x-1].append(y-1)
    g[y-1].append(x-1)

print(bfs(g, p1-1, p2-1, n, m))
