# 9252번 LCS 2
import sys

# main
s1 = sys.stdin.readline()
s2 = sys.stdin.readline()

# n(s1) : 세로, m(s2) : 가로
n = len(s1)  # '\n'도 포함되어 있음.
m = len(s2)

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(1,n):
    for j in range(1,m):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

maxLen = dp[n-1][m-1]
print(maxLen)

# 문자열 찾아내기
answer = []
x = m - 1
y = n - 1
while x > 0 and y > 0:
    if dp[y][x-1] == dp[y][x]:
        x -= 1
    elif dp[y-1][x] == dp[y][x]:
        y -= 1
    else:
        answer.append(s1[y-1])
        x -= 1
        y -= 1
    
for c in answer[::-1]:
    print(c, end='')
print()
