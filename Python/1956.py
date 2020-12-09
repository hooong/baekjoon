# 1956번 운동
from sys import stdin, maxsize
INF = maxsize

v, e = map(int, stdin.readline().split())
distance = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    distance[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

ans = INF
for i in range(1, v+1):
    ans = min(ans, distance[i][i])

print(-1 if ans == INF else ans)
