# 15664번 N과 M (10)
import sys

# printS
def printS(s):
    for i in s:
        print(i, end=' ')
    print()

# dfs
def dfs(cur, cnt, s):
    global arr_s, n, m

    if cnt == m:
        printS(s)
        return

    for i in range(cur,len(arr_s)):
        if not visited[i] == 0:
            visited[i] -= 1
            s.append(arr_s[i])
            dfs(i, cnt+1, s)
            visited[i] += 1
            s.pop()

# main
n, m = map(int, input().split())
arr = [int(x) for x in sys.stdin.readline().split()]
arr_s = list(set(arr))

arr_s.sort()
visited = [0 for _ in range(len(arr_s))]
for i in range(len(arr_s)):
    visited[i] = arr.count(arr_s[i])

for i in range(len(arr_s)):
    visited[i] -= 1
    dfs(i,1,[arr_s[i]])
    visited[i] += 1
