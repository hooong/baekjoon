# 15666번 N과 M (12)
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
        s.append(arr_s[i])
        dfs(i,cnt+1, s)
        s.pop()

# main
n, m = map(int, input().split())
arr = [int(x) for x in sys.stdin.readline().split()]
arr_s = list(set(arr))

arr_s.sort()
for i in range(len(arr_s)):
    dfs(i,1,[arr_s[i]])
