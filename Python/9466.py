# 9466번 텀 프로젝트
import sys

sys.setrecursionlimit(111111)
def dfs(cur):
    global visited, cnt, done

    visited[cur] = True
    ns = students[cur-1]
    if not visited[ns]:
        dfs(ns)
    else:
        if not done[ns]:
            i = ns
            while i != cur:
                cnt += 1
                i = students[i-1]
            cnt += 1
    done[cur] = True

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    students = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    done = [False] * (n+1)
    visited = [False] * (n+1)

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)

    print(n - cnt)
