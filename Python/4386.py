# 4386번 별자리 만들기
from sys import stdin
import math, heapq


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

    if rank[y] > rank[x]:
        x, y = y, x

    parent[y] = x

    if rank[x] == rank[y]:
        rank[y] += 1


def is_same(x, y):
    return find(x) == find(y)


n = int(stdin.readline())
points = []

for _ in range(n):
    x, y = map(float, stdin.readline().split())
    points.append([x, y])

q = []
for i in range(n-1):
    for j in range(i+1, n):
        a = points[i]
        b = points[j]
        diff = math.sqrt(pow(abs(a[0] - b[0]), 2) + pow(abs(a[1] - b[1]), 2))

        heapq.heappush(q, [diff, i, j])

parent = [0] * n
rank = [0] * n
total_cost = 0
for i in range(n):
    parent[i] = i

while q:
    cost, a, b = heapq.heappop(q)

    if not is_same(a, b):
        total_cost += cost
        union(a, b)

print(round(total_cost, 2))

