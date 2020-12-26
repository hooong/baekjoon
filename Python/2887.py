# 2887번 행성 터널
import sys, heapq


def find(x):
    global parent

    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    global parent, rank

    x = find(x)
    y = find(y)

    if x == y:
        return

    if rank[x] < rank[y]:
        x, y = y, x

    parent[y] = x

    if rank[x] == rank[y]:
        rank[y] += 1


def is_same(x, y):
    return find(x) == find(y)


n = int(sys.stdin.readline())

planet = []
for i in range(n):
    point = list(map(int, sys.stdin.readline().split()))
    planet.append([i] + point)

parent = [0] * n
rank = [1] * n
for i in range(n):
    parent[i] = i

q = []
planet.sort(key=lambda x: x[1])
for i in range(n-1):
    heapq.heappush(q, [abs(planet[i][1] - planet[i+1][1]), planet[i][0], planet[i+1][0]])

planet.sort(key=lambda x: x[2])
for i in range(n-1):
    heapq.heappush(q, [abs(planet[i][2] - planet[i+1][2]), planet[i][0], planet[i+1][0]])

planet.sort(key=lambda x: x[3])
for i in range(n-1):
    heapq.heappush(q, [abs(planet[i][3] - planet[i+1][3]), planet[i][0], planet[i+1][0]])

cnt = 0
answer = 0
while q:
    cost, a, b = heapq.heappop(q)

    if not is_same(a, b):
        answer += cost
        cnt += 1
        union(a, b)

    if cnt == n-1:
        break

print(answer)
