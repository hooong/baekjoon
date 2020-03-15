# 1753번 최단경로
import sys

# dijkstra algorithm
def dijkstra(v,k,g):
    inf = float('inf')

    # 방문 여부를 저장하는 배열
    visit = [False] * (v+1)

    # 최소 거리를 저장하는 배열
    d = [inf for _ in range(v+1)]
    d[k] = 0

    while True:
        min_d = inf

        for i in range(1,v+1):
            if not visit[i] and d[i] < min_d:
                min_d = d[i]
                node = i
        
        if min_d == inf:
            break
        
        visit[node] = True
        for i in range(1,v+1):
            if not visit[i]:
                via = d[node] + g[node][i]
                if via < d[i]:
                    d[i] = via
                print(d)
    
    print(visit)
    return d

# main
V, E = [int(x) for x in sys.stdin.readline().split()]

# 시작 노드
K = int(input())

# 인접행렬
g = [[float('inf') for _ in range(V+1)] for _ in range(V+1)]
for _ in range(E):
    v, e, w = [int(x) for x in sys.stdin.readline().split()]
    g[v][e] = w

answer = dijkstra(V,K,g)
for dis in answer:
    print(dis if dis != float('inf') else 'INF')



