# 1967번 트리의 지름
from collections import deque

def bfs(pos):
    global visited, max_dis, max_pos

    q = deque()
    q.append([pos, 0])
    while q:
        cur, dis = q.pop()

        for n_node, d in adj_list[cur]:
            if not visited[n_node]:
                visited[n_node] = True
                q.append([n_node, dis + d])
                if d + dis > max_dis:
                    max_dis = d + dis
                    max_pos = n_node

n = int(input())
adj_list = [[] for _ in range(n+1)]
max_dis = 0
max_pos = 0

for _ in range(n-1):
    a, b, c = map(int, input().split())
    adj_list[a].append([b, c])
    adj_list[b].append([a, c])

visited = [False] * (n+1)
bfs(1)

visited = [False] * (n+1)
max_dis = 0
bfs(max_pos)

print(max_dis)
