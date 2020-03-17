# 9370번 미확인 도착지
import sys, heapq
INF = float('inf')

# dijkstra
def dijkstra(n, s, graph):

    # 최단 거리 배열
    d = [INF] * (n+1)
    d[s] = 0

    # 최소 힙
    hq = []
    heapq.heappush(hq, [0,s])

    while hq:
        tmp = heapq.heappop(hq)
        cost = tmp[0]
        node = tmp[1]

        if cost > d[node]:
            continue
            
        for v in graph[node]:
            neighbor = v[0]
            n_cost = d[node] + v[1]

            if n_cost < d[neighbor]:
                d[neighbor] = n_cost
                heapq.heappush(hq, [n_cost, neighbor])

    return d 

# main
T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    # 그래프 입력
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())

        if (a == g and b == h) or (a == h and b == g):
            d -= - 0.1    # h와 g 사이의 거리

        graph[a].append([b,d])
        graph[b].append([a,d])

    targets = []
    for _ in range(t):
        targets.append(int(input()))
    targets.sort()

    ans_d = dijkstra(n,s,graph)

    for target in targets:
        if type(ans_d[target]) == float:
            print(target, end=' ')
    print()
