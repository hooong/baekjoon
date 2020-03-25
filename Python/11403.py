# 11403번 경로 찾기
import sys
from collections import deque

# bfs
def bfs(N, g, start, answer):    
    q = deque(g[start])
    visit = [False] * N

    while q:
        b_node = q.popleft()
        visit[b_node] = True
        answer[start][b_node] = 1

        for i in range(N):
            if i in g[b_node]:
                answer[b_node][i] = 1

                if not visit[i]:
                    q.append(i)
    
    return answer

# main
N = int(input())

# 그래프
g = []
for _ in range(N):
    row = [int(x) for x in sys.stdin.readline().split()]
    tmp = []

    for i in range(N):
        if row[i] == 1:
            tmp.append(i)

    g.append(tmp)


answer = [[0 for _ in range(N)] for _ in range(N)]
for node in range(N):
    answer = bfs(N,g,node,answer)

# 출력
for node in answer:
    for i in node:
        print(i, end=' ')
    print()
