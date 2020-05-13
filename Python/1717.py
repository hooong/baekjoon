# 1717번 집합의 표현
import sys

# find
def find(x):
    global parents

    while True:
        if parents[x] == x:
            return x
        else:
            x = parents[x]

# union
def union(x, y):
    global parents

    x = find(x)
    y = find(y)

    if not x == y:
        parents[y] = x

# main
n, m = map(int, input().split())
parents = [i for i in range(n+1)]

for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().split())

    if op == 0:
        union(a,b)
    else:
        if (find(a) == find(b)):
            print("yes")
        else:
            print("no")
