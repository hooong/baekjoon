# 2631번 줄세우기

# main
n = int(input())

children = []
for _ in range(n):
    children.append(int(input()))

# LIS
dp = [0 for _ in range(n)]
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if children[j] < children[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))