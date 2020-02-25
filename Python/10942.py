# 10942번 팰린드롬?
import sys

# main
n = int(sys.stdin.readline())
nums = [int(x) for x in sys.stdin.readline().split()]

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

i = n
while i > 0:
    j = n
    while j >= i:
        if i == j:
            dp[i][j] = 1
        elif j - i == 1 and nums[i-1] == nums[j-1]:
            dp[i][j] = 1
        elif nums[i-1] == nums[j-1] and dp[i+1][j-1] == 1:
            dp[i][j] = 1
        j -= 1
    i -= 1

m = int(sys.stdin.readline())
for _ in range(m):
    s, e = [int(x) for x in sys.stdin.readline().split()]
    print(dp[s][e])