# 20040번 사이클 게임
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def find(x):
    global parent

    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False

    if rank[x] < rank[y]:
        x, y = y, x

    parent[y] = x

    if rank[x] == rank[y]:
        rank[y] += 1

    return True


n, m = map(int, stdin.readline().split())

parent = [0] * n
rank = [1] * n
for i in range(n):
    parent[i] = i

for i in range(1, m+1):
    a, b = map(int, stdin.readline().split())

    if not union(a, b):
        print(i)
        break
else:
    print(0)
