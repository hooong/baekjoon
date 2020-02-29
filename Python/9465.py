# 9465번 스티커
import sys

# main
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    st = [[int(x) for x in sys.stdin.readline().split()] for _ in range(2)]

    dp = [[0 for _ in range(n+1)] for _ in range(3)]

    # 1행
    dp[1][1] = st[0][0]
    for j in range(2,n+1):
        dp[1][j] = dp[1][j-2] + st[0][j-1]

    # 2행
    dp[2][1] = st[1][0]
    for j in range(2,n+1):
        dp[2][j] = max(dp[1][j-2], dp[1][j-1]+dp[2][j-2]) + st[1][j-1]
    
    print(max(dp[2]))