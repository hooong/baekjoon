# 2294번 동전 2

# main
n, k = map(int, input().split())

# 동전 가치 입력, 정렬
coin = [0]
for _ in range(n):
    tmp = int(input())
    if not tmp in coin:
        coin.append(tmp)
coin.sort()

dp = [[0 for _ in range(k+1)] for _ in range(len(coin))]
dp[0][0] = 1

for i in range(1,len(coin)):
    dp[i][0] = 1
    for j in range(1,k+1):
        if (coin[i] <= j):
            dp[i][j] += dp[]

print(dp[:][1])
# if min(dp[:][k]) == 10001:
#     print(-1)
# else:
#     print(min(dp[:][k]))


