# 1965번 상자넣기
import sys

# main
n = int(input())
box = [int(x) for x in sys.stdin.readline().split()]

dp = [1 for _ in range(n+1)]

if n == 1:
    print(1)
else:
    for i in range(2,n+1):
        for j in range(1,i+1):
            if box[j-1] < box[i-1]:
                dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))