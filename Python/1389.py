# 1389번 케빈 베이컨의 6단계 법칙
import sys
INF = float('inf')

# main
N, M = [int(x) for x in sys.stdin.readline().split()]

# 각 관계에 대하여 최단 거리를 저장
relation = [[INF for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y = [int(x) for x in sys.stdin.readline().split()]

    # 테이블 초기화 (인접한 정점과의 거리)
    relation[x-1][y-1] = 1
    relation[y-1][x-1] = 1

# 플로이드-와샬 알고리즘
for k in range(N):      # 한 점을 경유
    for i in range(N):      # i에서 출발
        for j in range(N):  # j로 도착
            relation[i][j] = min(relation[i][j], relation[i][k] + relation[k][j])

# 케빈 베이컨 수
kebin = []
for i in range(N):
    dSum = 0
    for j in range(N):
        dSum += relation[i][j]
    kebin.append(dSum)

print(kebin.index(min(kebin)) + 1)
