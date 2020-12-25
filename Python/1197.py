# 1197번 최소 스패닝 트리
from sys import stdin
import heapq


def find(x):
    global parent

    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if rank[x] < rank[y]:
        x, y = y, x

    parent[y] = x

    if rank[x] == rank[y]:
        rank[x] += 1


def is_same(x, y):
    return find(x) == find(y)


v, e = map(int, stdin.readline().split())
total_cost = 0

parent = [0] * (v+1)
rank = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

que = []
for _ in range(e):
    a, b, cost = map(int, stdin.readline().split())
    heapq.heappush(que, [cost, a, b])

while que:
    cost, a, b = heapq.heappop(que)

    if not is_same(a, b):
        union(a, b)
        total_cost += cost

print(total_cost)
