# 9465번 스티커
import sys

# main
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    st = [[int(x) for x in sys.stdin.readline().split()] for _ in range(2)]

    if n == 1:
        print(max(st[0][0],st[1][0]))
    else:
        dp = [[0 for _ in range(3)] for _ in range(n+1)]
        
        dp[1][1] = st[0][0]
        dp[1][2] = st[1][0]
        for i in range(2,n+1):
            for j in range(1,3):
                if j == 1:
                    dp[i][j] = max(dp[i-1][j+1],dp[i-2][j+1]) + st[j-1][i-1]
                else:
                    dp[i][j] = max(dp[i-1][j-1],dp[i-2][j-1]) + st[j-1][i-1]

        print(max(dp[n]))