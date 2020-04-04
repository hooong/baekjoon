# 1389번 케빈 베이컨의 6단계 법칙
import sys
INF = float('inf')

# main
N, M = [int(x) for x in sys.stdin.readline().split()]

# [직전 정점, 거리]
relation = [[INF for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y = [int(x) for x in sys.stdin.readline().split()]

    # 테이블 초기화
    relation[x-1][y-1] = 1
    relation[y-1][x-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            relation[i][j] = min(relation[i][j], relation[i][k] + relation[k][j])

# 케빈 베이컨 수
kebin = []
for i in range(N):
    dSum = 0
    for j in range(N):
        dSum += relation[i][j]
    kebin.append(dSum)

print(kebin.index(min(kebin)) + 1)
