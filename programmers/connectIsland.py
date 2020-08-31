# Kruskal
parent = dict()

def make_set(v):
    parent[v] = v

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)

    parent[root2] = root1

def solution(n, costs):
    answer = 0

    for i in range(n):
        make_set(i)

    edges = []
    for cost in costs:
        edges.append([cost[2], cost[0], cost[1]])

    edges.sort()

    for edge in edges:
        weight, v1, v2 = edge
        if find(v1) != find(v2):
            union(v1, v2)
            answer += weight

    return answer

if __name__ == '__main__':
    print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))