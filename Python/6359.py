# 6359번 만취한 상범
import sys

# main
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    # 0 : 닫힘, 1 : 열림
    dp = [0 for _ in range(n+1)]
    for k in range(1,n+1):
        tmp = k
        i = 2
        
        while tmp <= n:
            if dp[tmp] == 0:
                dp[tmp] = 1
            else:
                dp[tmp] = 0

            tmp = k * i
            i += 1

    print(dp.count(1))


