# 2225번 합분해

# main
n, k = map(int, input().split())

dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
dp[1] = [1 for _ in range(n+1)]

for i in range(1,k+1):
    for j in range(n+1):
        for a in range(j+1):
            dp[i][j] += dp[i-1][j-a]
            dp[i][j] %= 1000000000
print(dp[k][n])
            
