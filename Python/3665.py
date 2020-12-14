# 3665번 최종 순위
from sys import stdin
from collections import deque


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    rank = list(map(int, stdin.readline().split()))
    rank_info = [[False] * (n+1) for _ in range(n+1)]
    in_degree = [0] * (n+1)

    for i in range(n):
        for j in range(i+1, n):
            # i번째가 j번째보다 앞에 있음을 체크
            rank_info[rank[i]][rank[j]] = True

    m = int(stdin.readline())
    for _ in range(m):
        a, b = map(int, stdin.readline().split())

        # 순위에 변동이 있다면 두 개의 값을 변경
        rank_info[a][b], rank_info[b][a] = rank_info[b][a], rank_info[a][b]

    final_rank = []     # 최종 순위를 저장
    q = deque()
    for i in range(1, n+1):
        in_degree[i] = rank_info[i].count(True)     # 진입차수를 계산
        if in_degree[i] == 0:
            q.append(i)

    # 위상정렬 알고리즘
    while q:
        cur = q.popleft()
        final_rank.append(cur)

        for i in range(1, n+1):
            if rank_info[i][cur]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    q.append(i)

    if len(final_rank) == n:
        print(*final_rank[::-1])
    else:
        print("IMPOSSIBLE")
