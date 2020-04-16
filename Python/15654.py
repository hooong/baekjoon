# 15654번 N과 M (5)
import sys

# printS
def printS(s):
    for i in s:
        print(i, end=' ')
    print()

# dfs
def dfs(cnt, s):
    global arr, n

    if cnt == m:
        printS(s)
        return

    for i in range(n):
        if not visited[i]: 
            visited[i] = True
            s.append(arr[i])
            dfs(cnt+1, s)
            visited[i] = False
            s.pop()

# main
n, m = map(int, input().split())
arr = [int(x) for x in sys.stdin.readline().split()]
arr.sort()

visited = [False for _ in range(n)]
for i in range(n):
    visited[i] = True
    dfs(1,[arr[i]])
    visited[i] = False
