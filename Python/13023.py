# 13023번 ABCDE
from collections import deque
import sys

# dfs 
def find(cur, cnt):
    global friends, visited

    if cnt == 5:
        return True
    
    for f in friends[cur]:
        if not visited[f]:
            visited[f] = True
            if find(f, cnt+1):
                return True
            visited[f] = False
    return False    

# main
n, m = map(int, sys.stdin.readline().split())

friends = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

visited = [False for _ in range(n)]
# bfs
for i in range(n):
    visited[i] = True
    isABCDE = find(i,1)
    visited[i] = False

    if isABCDE:
        break

print(1 if isABCDE else 0)