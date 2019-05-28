t = int(input())
apart = [[0]*15 for i in range(15)]     # index에러를 없애기 위해서 15*15로 선언
result = []

for _ in range(t):
    k = int(input())
    n = int(input())

    for i in range(k+1):
        for j in range(1,n+1):
            if i == 0 or j == 1:        # 0층 i호는 i명 사는것과 각층의 1호는 1명이 사는 조건
                apart[i][j] = j
            else:
                apart[i][j] = apart[i][j-1] + apart[i-1][j]         # 규칙성

    result.append(apart[k][n])

for i in result:
    print(i)