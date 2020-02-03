# 2740번 행렬 곱셈

# 입력
n, m = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(n)]

m, k = map(int, input().split())
b = [list(map(int,input().split())) for _ in range(m)]

# 곱셈
result = [[0 for _ in range(n)] for _ in range(k)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            result[i][j] += a[i][l] * b[l][j]

# 출력
for row in result:
    for num in row:
        print(num, end=' ')
    print()
