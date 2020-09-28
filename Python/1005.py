# ACM Craft
from collections import deque

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))

    pre = [0 for _ in range(n)]
    suc = [[] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        pre[b-1] += 1
        suc[a-1].append(b-1)

    target = int(input()) - 1

    min_time = [0 for _ in range(n)]
    q = deque()
    for i in range(n):
        if pre[i] == 0:
            q.append(i)

    while q:
        i = q.popleft()

        if pre[target] == 0:
            print(min_time[target] + time[target])
            break

        for s in suc[i]:
            min_time[s] = max(min_time[s], min_time[i] + time[i])

            pre[s] -= 1
            if pre[s] == 0:
                q.append(s)
