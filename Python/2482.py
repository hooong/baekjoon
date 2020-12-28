# 2482번 색상환

n = int(input())
k = int(input())
dp = [[0] * (k+1) for _ in range(n+1)]

# dp 테이블 초기화
for i in range(n+1):
    dp[i][0] = 1
    dp[i][1] = i

# 선형일때, 경우의 수
for i in range(2, n+1):
    for j in range(2, k+1):
        dp[i][j] = (dp[i-2][j-1] + dp[i-1][j]) % 1000000003

answer = (dp[n-3][k-1] + dp[n-1][k]) % 1000000003      # 원형으로 생각할때의 경우의 수
print(answer)