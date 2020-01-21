n = int(input())

# 삼각형 입력
tri = []
for i in range(n):
    tri.append([])
    nums = input().split()
    for num in nums:
        tri[i].append(int(num))

dp = []
for i in range(0,n):
    dp.append([])
    # 맨꼭대기 하나를 저장.
    if i == 0:
        dp[i].append(tri[0][0])
    else:
        for j in range(i+1):
            if j == 0:      # 맨 왼쪽은 바로 위 오른쪽만 더할 수 있다.
                dp[i].append(dp[i-1][0] + tri[i][0])
            elif j == i:    # 맨 마지막은 바로 위 왼쪽만 더할 수 있다.
                dp[i].append(dp[i-1][j-1] + tri[i][j])
            else:           # 나머지 경우는 2차원 배열로 봤을때 바로위 왼쪽과 바로위에 두개에 접근가능.
                dp[i].append(max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j])

print(max(dp[n-1]))


