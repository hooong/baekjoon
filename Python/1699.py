# 1699번 제곱수의 합
import math

# main
n = int(input())
root_n = int(math.sqrt(n))

dp = [0 for _ in range(n+1)]

for i in range(1,root_n+1):
    if i == 1:
        for j in range(1,n+1):
            dp[j] = j
    else:
        for j in range(1,n+1):
            if j - (i**2) < 0:
                dp[j] = dp[j]
            else:
                dp[j] = min(dp[j-(i**2)]+1, dp[j])
print(dp[-1])
