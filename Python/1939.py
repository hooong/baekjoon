# 1939번 중량제한
from collections import deque

n, m = map(int, input().split())

max_c = 0
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append([b, c])
    adj[b].append([a, c])
    max_c = max(max_c, c)

start, end = map(int, input().split())

left = 0
right = max_c
while left <= right:
    mid = (left + right) // 2

    dq = deque()
    dq.append(start)
    visited = [False for _ in range(n+1)]
    visited[start] = True
    while dq:
        cur = dq.popleft()

        if cur == end:
            break

        for i, c in adj[cur]:
            if not visited[i] and mid <= c:
                visited[i] = True
                dq.append(i)

    if visited[end]:
        left = mid + 1
    else:
        right = mid - 1

print(right)
