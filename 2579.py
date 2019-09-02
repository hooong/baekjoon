# n번째 계단에 도달할 수 있는 경우의 수는 두가지이다.
# 1. n-1번 계단을 거치는 경우 => 두번 연속 한칸은 못가므로 n-3을 꼭 거쳐야함
#     ==>  dp[i] = dp[n-3] + stair[n-1] + stair[n]
# 2. n-1번 계단을 거치지 않는 경우로 ==> n-2번째에서 바로 n번째로 온다.
#     ==>  dp[i] = dp[n-2] + stair[n]

n = int(input())

stair = [0]
for _ in range(n):
    stair.append(int(input()))

dp = [0]
# 1일경우 1만 더한다
if n == 1:
    print(stair[1])
# 2일경우 1과 2를 더한다.
elif n == 2:
    print(stair[1]+stair[2])
# 아닌 경우 1과 2를 저장해주고 3부터는 위에 경우 두가지중 큰값을 dp에 저장한다.
else:
    dp.append(stair[1])
    dp.append(stair[1]+stair[2])
    for i in range(3,n+1):
        dp.append(max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i]))
    print(dp[n])
    
