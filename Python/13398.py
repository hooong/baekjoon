# 13398번 연속합 2
import sys

# main
n = int(input())
arr = [int(x) for x in sys.stdin.readline().split()]

dp = [[0 for _ in range(2)] for _ in range(n)]
dp[0][0] = dp[0][1] = arr[0]

answer = -100000000
for i in range(1,n):
    # 제거를 하지 않을 때의 최댓값
    dp[i][0] = max(arr[i], dp[i-1][0] + arr[i])
    # i-1의 값을 제거하는 경우의 최댓값
    dp[i][1] = max(dp[i-1][0], dp[i-1][1] + arr[i])

    answer = max(answer, max(dp[i]))

print(answer)
