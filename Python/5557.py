# 5557번 1학년
import sys

# main
N = int(input())

nums = [int(x) for x in sys.stdin.readline().split()]
result = nums.pop()     # 계산 결과 값

# dp[숫자 개수 - 1][21]
dp = [[0 for _ in range(21)] for _ in range(len(nums))]

dp[0][nums[0]] = 1
for i in range(len(nums)-1):
    for j in range(21):
        if not dp[i][j] == 0:
            # 더하기
            plus = j + nums[i+1]
            if plus <= 20:
                dp[i+1][plus] += dp[i][j]

            # 빼기
            minus = j - nums[i+1]
            if 0 <= minus:
                dp[i+1][minus] += dp[i][j]

print(dp[-1][result])
