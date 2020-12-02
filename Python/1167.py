# 1167번 트리의 지름
from collections import deque

def bfs(position):
    global max_dis, max_pos, visited

    q = deque()
    q.append([position,0])
    while q:
        cur, dis = q.pop()

        visited[cur] = True
        for n_node, d in adj_list[cur]:
            if not visited[n_node]:
                visited[n_node] = True
                q.append([n_node, dis + d])

                if dis + d > max_dis:
                    max_dis = dis + d
                    max_pos = n_node


n = int(input())
visited = [False] * (n+1)
max_dis = 0
max_pos = 0

adj_list = [[] for _ in range(n+1)]
for _ in range(n):
    tmp = list(map(int, input().split()))

    node = tmp.pop(0)
    while not tmp[0] == -1:
        n_node = tmp.pop(0)
        d = tmp.pop(0)

        adj_list[node].append([n_node, d])

bfs(1)

visited = [False] * (n+1)
max_dis = 0

bfs(max_pos)

print(max_dis)
