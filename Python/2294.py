# 2294번 동전 2
import sys

n, k = map(int, input().split())

coins = []
for _ in range(n):
    tmp = int(input())
    if not tmp in coins:
        coins.append(tmp)
coins.sort()

dp = [sys.maxsize] * (k+1)
dp[0] = 0
for i in range(len(coins)):
    for j in range(coins[i], k+1):
        dp[j] = min(dp[j], dp[j-coins[i]]+1)

if dp[-1] == sys.maxsize:
    print(-1)
else:
    print(dp[-1])
