# 10164번 격자상의 경로
import sys

# 경로 수 구하는 함수
def find(y,x):
    dp = [[0 for _ in range(x+1)] for _ in range(y+1)]

    for i in range(1,y+1):
        for j in range(1,x+1):
            if i == 1 and j == 1:
                dp[i][j] = 1
                continue

            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[y][x]

# main
n, m, k = [int(x) for x in sys.stdin.readline().split()]

if k == 0:      # 중간지점이 없는 경우
    print(find(n,m))

else:       # 중간지점이 있는 경우
    dotN1 = (k-1) // m + 1
    dotM1 = k - (dotN1-1) * m
    dotN2 = n - (dotN1-1)
    dotM2 = m - (dotM1-1)

    # 왼쪽 위 경로
    r1 = find(dotN1,dotM1)
    # 오른쪽 아래 경로
    r2 = find(dotN2,dotM2)

    print(r1*r2)
