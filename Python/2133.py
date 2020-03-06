# 2133번 타일 채우기

# main
n = int(input())

dp = [1] * 31
if not n % 2 == 0:
    print(0)
else:
    dp[2] = 3
    for i in range(4,n+1):
        dp[i] = dp[i-2] * 3     # 보통의 경우

        for j in range(4,i+1,2):  # 가운데가 1*2로 차는 경우
            dp[i] += dp[i-j] * 2
    print(dp[n])