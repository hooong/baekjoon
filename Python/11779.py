# 11779번 최소비용 구하기 2
import sys, heapq
INF = sys.maxsize

n = int(sys.stdin.readline())

adj_list = [[] for _ in range(n+1)]
for _ in range(int(sys.stdin.readline())):
    x, y, c = map(int, sys.stdin.readline().split())
    adj_list[x].append([y, c])

a, b = map(int, sys.stdin.readline().split())

dis = [INF] * (n+1)
q = []
heapq.heappush(q, [0, a])
dis[a] = 0
trace = [[] for _ in range(n+1)]
while q:
    cur_cost, cur_city = heapq.heappop(q)

    if cur_city == b:
        print(cur_cost)

        path = [b]
        while b != a:
            path.append(trace[b])
            b = trace[b]

        print(len(path))
        print(*path[::-1])
        break

    for next_city, cost in adj_list[cur_city]:
        if dis[next_city] <= cur_cost + cost:
            continue

        dis[next_city] = cur_cost + cost
        trace[next_city] = cur_city
        heapq.heappush(q, [cur_cost + cost, next_city])




