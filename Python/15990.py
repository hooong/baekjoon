# 15990번 1,2,3 더하기 5

# main
dp = [[0 for _ in range(4)] for _ in range(100001)]
dp[1] = [0,1,0,0]
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]

for i in range(4,100001):
    for j in range(1,4):
        # j로 시작하는 식의 수
        dp[i][j] = (sum(dp[i-j]) - dp[i-j][j]) % 1000000009 

t = int(input())

for _ in range(t):
    n = int(input())
    print(sum(dp[n]) % 1000000009)
    