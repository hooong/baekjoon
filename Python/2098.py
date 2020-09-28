# 외판원 순회
import sys

def tsp(cur, visited):
    if visited == (1 << n) - 1:
        if not graph[cur][0] == 0:
            return graph[cur][0]
        else:
            return sys.maxsize

    if not mask[cur][visited] == -1:
        return mask[cur][visited]
    
    cost = sys.maxsize
    for i in range(n):
        if not visited & (1 << i) == 0:
            continue
        if graph[cur][i] == 0:
            continue
        cost = min(cost, tsp(i, visited | (1 << i)) + graph[cur][i])
    mask[cur][visited] = cost
    return cost

n = int(sys.stdin.readline())
graph = [list(map(int, input().split())) for _ in range(n)]
mask = [[-1] * (1 << n) for _ in range(n)]

print(tsp(0,1))
