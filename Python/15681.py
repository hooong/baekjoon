# 15681번 트리와 쿼리
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def dfs(root):
    global cnt, visited

    if cnt[root] != 0:
        return cnt[root]

    visited[root] = True

    tmp = 1
    for ch in adj_list[root]:
        if not visited[ch]:
            tmp += dfs(ch)
    cnt[root] = tmp
    return tmp


n, r, q = map(int, stdin.readline().split())
adj_list = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

cnt = [0] * (n + 1)
cnt[r] = dfs(r)

for _ in range(q):
    i = int(stdin.readline())
    print(cnt[i])
