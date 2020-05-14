# 1976번 여행 가자
import sys

# find
def find(x):
    global parents

    while True:
        if parents[x] == x:
            return x
        x = parents[x]

# union
def union(a,b):
    global parents

    a = find(a)
    b = find(b)

    if not a == b:
        parents[b] = a

# main
n = int(input())
m = int(input())

graph = []
for _ in range(n):
    graph.append([int(x) for x in sys.stdin.readline().split()])

parents = [int(x) for x in range(n+1)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i+1,j+1)

travel = [int(x) for x in sys.stdin.readline().split()]

root = find(travel[0])
isDis = True
for t in travel:
    if not root == find(t):
        isDis = False
        break

print("YES" if isDis else "NO")
