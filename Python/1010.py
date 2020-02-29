# 1010번 다리 놓기

# 이항계수 배열 생성
dp = [[0 for _ in range(30)] for _ in range(30)]

for i in range(30):
    for j in range(i+1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

# main
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(dp[m][n])
