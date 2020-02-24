# 11066번 파일 합치기
import sys

# main
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    parr = [int(x) for x in sys.stdin.readline().split()]

    psum = [0] * (n+1)
    for i in range(1,n+1):
        psum[i] = psum[i-1] + parr[i-1]

    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(2,n+1):
        j = i - 1
        while j > 0:
            dp[j][i] = 100000000
            k = j
            while k < i:
                dp[j][i] = min(dp[j][i], dp[j][k] + dp[k+1][i])
                k += 1

            dp[j][i] += psum[i] - psum[j-1]
            j -= 1
    print(dp[1][n])