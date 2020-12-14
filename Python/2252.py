# 2252번 줄 세우기
from collections import deque
import sys


n, m = map(int, sys.stdin.readline().split())
students = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)

for _ in range(m):
    s1, s2 = map(int, sys.stdin.readline().split())
    students[s1].append(s2)
    in_degree[s2] += 1

q = deque()
for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    print(cur, end=' ')

    for s in students[cur]:
        in_degree[s] -= 1
        if in_degree[s] == 0:
            q.append(s)
