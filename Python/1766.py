# 1766번 문제집
from sys import stdin
import heapq


n, m = map(int, stdin.readline().split())
problems = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    in_degree[b] += 1
    problems[a].append(b)

hq = []
for i in range(1, n+1):
    if in_degree[i] == 0:
        heapq.heappush(hq, i)

while hq:
    cur = heapq.heappop(hq)
    print(cur, end=' ')

    for k in problems[cur]:
        in_degree[k] -= 1
        if in_degree[k] == 0:
            heapq.heappush(hq, k)
