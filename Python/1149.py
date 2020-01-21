n = int(input())

costs = []
for _ in range(n):
    r,g,b = map(int,input().split())
    costs.append([r,g,b])

# dp => 색깔들중 현재 고른 색과 여태까지의 최소값을 더해서 저장.
dp = [[costs[0][0], costs[0][1], costs[0][2]]]

for i in range(1,n):
    dp.append([])
    dp[i].append(min(dp[i-1][1], dp[i-1][2]) + costs[i][0])
    dp[i].append(min(dp[i-1][0], dp[i-1][2]) + costs[i][1])
    dp[i].append(min(dp[i-1][0], dp[i-1][1]) + costs[i][2])  

minimum_cost = min(dp[n-1][0], dp[n-1][1], dp[n-1][2])
print(minimum_cost)
