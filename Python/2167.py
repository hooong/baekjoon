# 2167번 2차원 배열의 합
import sys

# main
n, m = [int(x) for x in sys.stdin.readline().split()]
arr = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]

# 합에 대한 dp 생성
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i][j-1] + arr[i-1][j-1]

# 범위 합 구하기
k = int(sys.stdin.readline())
for _ in range(k): 
    i, j, x, y = [int(x) for x in sys.stdin.readline().split()]

    result = 0
    for r in range(i,x+1):
        result += dp[r][y] - dp[r][j-1]
    
    print (result)