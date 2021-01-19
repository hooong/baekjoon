# 4803번 트리
from sys import stdin
from collections import deque


case = 1
while True:
    n, m = map(int, stdin.readline().split())

    if n == 0 and m == 0:
        break

    adj_list = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    q = deque()
    cnt = 0
    for i in range(1, n + 1):
        if visited[i]:
            continue

        q.append(i)

        edge = 0
        vertex = 0
        while q:
            cur = q.popleft()

            if visited[cur]:
                continue

            vertex += 1
            visited[cur] = True

            for node in adj_list[cur]:
                edge += 1
                q.append(node)

        if edge // 2 == vertex - 1:
            cnt += 1

    if cnt == 0:
        print("Case {}: No trees.".format(case))
    elif cnt == 1:
        print("Case {}: There is one tree.".format(case))
    else:
        print("Case {}: A forest of {} trees.".format(case, cnt))

    case += 1
