# 11726번 2*n타일링

n = int(input())
dp = [0] * (n+1)
            
for i in range(1,n+1):
    if i == 1:
        dp[1] = 1
    elif i == 2:
        dp[2] = 2
    else:
        dp[i] = (dp[i-2] + dp[i-1]) % 10007
    
print(dp[n] % 10007)