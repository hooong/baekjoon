# 9019번 DSLR
import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())

    visited = [False] * 10000
    q = deque()
    q.append([a, ''])
    visited[a] = True
    while q:
        cur, path = q.popleft()

        if cur == b:
            for ep in path:
                print(ep, end='')
            print()
            break

        # D
        d = (cur * 2) % 10000
        if not visited[d]:
            visited[d] = True
            q.append([d, path + 'D'])

        # S
        s = 9999 if cur - 1 < 0 else cur - 1
        if not visited[s]:
            visited[s] = True
            q.append([s, path + 'S'])

        # L
        l = (cur % 1000) * 10 + (cur // 1000)
        if not visited[l]:
            visited[l] = True
            q.append([l, path + 'L'])

        # R
        r = (cur % 10) * 1000 + (cur // 10)
        if not visited[r]:
            visited[r] = True
            q.append([r, path + 'R'])
