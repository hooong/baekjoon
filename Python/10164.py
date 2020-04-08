# 10164번 격자상의 경로
import sys

# main
n, m, k = [int(x) for x in sys.stdin.readline().split()]

if k == 0:      # 중간지점이 없는 경우
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:
                dp[i][j] = 1
                continue

            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    print(dp[n][m])

else:       # 중간지점이 있는 경우
    dotN1 = (k-1) // m + 1
    dotM1 = k - (dotN1-1) * m
    dotN2 = n - (dotN1-1)
    dotM2 = m - (dotM1-1)

    dp1 = [[0 for _ in range(dotM1+1)] for _ in range(dotN1+1)]
    dp2 = [[0 for _ in range(dotM2+1)] for _ in range(dotN2+1)]

    # dp1 경로
    for i in range(1,dotN1+1):
        for j in range(1,dotM1+1):
            if i == 1 and j == 1:
                dp1[i][j] = 1
                continue

            dp1[i][j] = dp1[i-1][j] + dp1[i][j-1]

    # dp2 경로
    for i in range(1,dotN2+1):
        for j in range(1,dotM2+1):
            if i == 1 and j == 1:
                dp2[i][j] = 1
                continue

            dp2[i][j] = dp2[i-1][j] + dp2[i][j-1]

    print(dp1[dotN1][dotM1] * dp2[dotN2][dotM2])