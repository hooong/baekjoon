# 1753번 최단경로
import sys, heapq

# 최대값(INF) 변수 선언
inf = float('inf')

# dijkstra algorithm
def dijkstra(v,k,g):

    # 최소 거리를 저장하는 배열
    d = [inf for _ in range(v+1)]
    d[k] = 0

    hq = []
    heapq.heappush(hq, [0,k])   # heapq에 [cost,node] 넣음.

    while hq:
        tmp = heapq.heappop(hq)     # cost가 최소인 노드 pop
        cost = tmp[0]
        node = tmp[1]

        if cost > d[node]:
            continue

        for n in g[node]:
            neighbor = n[0]
            n_cost = d[node] + n[1]

            if n_cost < d[neighbor]:
                d[neighbor] = n_cost
                heapq.heappush(hq, [n_cost,neighbor])

    return d

# main
V, E = [int(x) for x in sys.stdin.readline().split()]

# 시작 노드
K = int(input())

# 인접리스트
g = [[] for _ in range(V+1)]
for _ in range(E):
    v, e, w = [int(x) for x in sys.stdin.readline().split()]
    g[v].append([e,w])

answer = dijkstra(V,K,g)

for dis in answer[1:]:
    print(dis if dis != inf else 'INF')
