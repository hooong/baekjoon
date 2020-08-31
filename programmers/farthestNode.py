import heapq, sys

def solution(n, edge):
    global adj, d

    adj = [[] for _ in range(n+1)]
    d = [sys.maxsize for _ in range(n+1)]

    for e in edge:
        a = e[0]
        b = e[1]

        adj[a].append(b)
        adj[b].append(a)

    dijkstra(1)

    farthest = max(d[1:])
    answer = d.count(farthest)

    return answer

def dijkstra(s):
    heap = []

    d[s] = 0
    heapq.heappush(heap, [0,s])

    while heap:
        cur = heapq.heappop(heap)
        cur_distance = cur[0]
        cur_node = cur[1]

        if d[cur_node] < cur_distance:
            continue

        for node in adj[cur_node]:
            if cur_distance + 1 < d[node]:
                d[node] = cur_distance + 1
                heapq.heappush(heap, [cur_distance + 1, node])



if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))