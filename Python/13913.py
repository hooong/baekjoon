# 13913번 숨바꼭질 4
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

n, k = map(int, input().split())
street = [False] * 100001
path = [-1] * 100001

q = deque()
q.append([n, 0])
street[n] = True
while q:
    cur, time = q.popleft()

    if cur == k:
        print(time)

        tmp = []
        while k != n:
            tmp.append(k)
            k = path[k]
        tmp.append(n)
        print(*tmp[::-1])

        break

    if cur * 2 < 100001 and not street[cur * 2]:
        street[cur * 2] = True
        q.append([cur * 2, time + 1])
        path[cur * 2] = cur
    if cur + 1 < 100001 and not street[cur + 1]:
        street[cur + 1] = True
        q.append([cur + 1, time + 1])
        path[cur + 1] = cur
    if 0 <= cur - 1 and not street[cur - 1]:
        street[cur - 1] = True
        q.append([cur - 1, time + 1])
        path[cur - 1] = cur

