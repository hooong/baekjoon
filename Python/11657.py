# 11657번 타임머신
import sys
INF = sys.maxsize

n, m = map(int, input().split())
distance = [INF] * (n+1)
adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    adj_list[a].append([b, c])

distance[1] = 0
for i in range(n):
    is_update = False
    for cur in range(1, n+1):
        if distance[cur] == INF:
            continue

        for node, cost in adj_list[cur]:
            if distance[node] > distance[cur] + cost:
                distance[node] = distance[cur] + cost
                is_update = True
    if not is_update:
        break

if is_update:
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
