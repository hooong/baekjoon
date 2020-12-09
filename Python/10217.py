#10217번 KCM Travel
# from sys import stdin, maxsize
# import heapq
# INF = maxsize
#
# t = int(stdin.readline())
#
# for _ in range(t):
#     n, m, k = map(int, stdin.readline().split())
#     adj_list = [[] for _ in range(n+1)]
#     distance = [[INF] * (m+1) for _ in range(n+1)]
#     visited = [[False] * (m+1) for _ in range(n+1)]
#
#     for _ in range(k):
#         u, v, c, d = map(int, stdin.readline().split())
#         adj_list[u].append([d, c, v])
#
#     distance[1][0] = 0
#     visited[1][0] = True
#     q = []
#     heapq.heappush(q, [0, 0, 1])
#     while q:
#         h_dis, h_cost, here = heapq.heappop(q)
#
#         if h_dis > distance[here][h_cost]:
#             continue
#
#         for t_dis, t_cost, there in adj_list[here]:
#             if h_cost + t_cost > m:
#                 continue
#
#             if not visited[there][h_cost + t_cost] or distance[there][h_cost + t_cost] > h_dis + t_dis:
#                 visited[there][h_cost + t_cost] = True
#                 # for i in range(h_cost + t_cost, m+1):
#                 #     if distance[there][i] > h_dis + t_dis:
#                 distance[there][h_cost + t_cost] = h_dis + t_dis
#
#                 heapq.heappush(q, [h_dis + t_dis, h_cost + t_cost, there])
#
#     answer = min(distance[n])
#     if answer == INF:
#         print("Poor KCM")
#     else:
#         print(answer)

import sys

INF = sys.maxsize
for _ in range(int(sys.stdin.readline())):
    n, m, k = map(int, sys.stdin.readline().split())

    adj_list = [[] for _ in range(n+1)]
    for _ in range(k):
        u, v, c, d = map(int, sys.stdin.readline().split())
        adj_list[u].append([v, c, d])

    dp = [[INF] * (m+1) for _ in range(n+1)]
    dp[1][0] = 0
    for money in range(m+1):
        for here in range(1, n+1):
            if dp[here][money] == INF:
                continue

            h_dis = dp[here][money]
            for there, t_m, t_d in adj_list[here]:
                if money + t_m > m:
                    continue
                dp[there][money + t_m] = min(dp[there][money + t_m], h_dis + t_d)

    answer = min(dp[n])
    print("Poor KCM" if answer == INF else answer)
