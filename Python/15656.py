# 15656번 N과 M (7)
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
        s.append(arr[i])
        dfs(cnt+1, s)
        s.pop()

# main
n, m = map(int, input().split())
arr = [int(x) for x in sys.stdin.readline().split()]
arr.sort()

for i in range(n):
    dfs(1,[arr[i]])
