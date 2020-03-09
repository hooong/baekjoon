# 2606번 바이러스
import sys

# dfs
def dfs(v):
    visit[v] = 1
    
    for i in range(1,n+1):
        if visit[i] == 0 and net[v][i] == 1:
            dfs(i)

# main
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

net = [[0 for _ in range(n+1)] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for _ in range(m):
    i, j = [int(x) for x in sys.stdin.readline().split()]
    net[i][j] = 1
    net[j][i] = 1

dfs(1)
print(visit.count(1)-1)