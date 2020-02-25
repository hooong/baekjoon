# 7579번 앱
import sys

# main
n, m = [int(x) for x in sys.stdin.readline().split()]
run = [int(x) for x in sys.stdin.readline().split()]    # 사용중인 프로그램
cost = [int(x) for x in sys.stdin.readline().split()]   # 비활성화 비용

tc = sum(cost)

dp = [[0 for _ in range(n+1)] for _ in range(tc+1)]

for i in range(1,tc+1):
    for j in range(1,n+1):
        if i >= cost[j-1]:
            dp[i][j] = max(dp[i][j-1], dp[i-cost[j-1]][j-1] + run[j-1])
        else:
            dp[i][j] = dp[i][j-1]
    if max(dp[i]) >= m:
        print(i)
        break
