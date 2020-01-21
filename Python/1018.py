n, m = map(int,input().split())

board = []
for _ in range(n):
    board.append(list(input()))

result = []
for i in range(n-7):
    for j in range(m-7):
        re_1 = 0        # 맨 왼쪽 위가 'W'
        re_2 = 0        # 맨 왼쪽 위가 'B'
        # 전체 판에서 8*8이 가능한 모든 경우의 수 따져보기
        for k in range(i,i+8):
            for l in range(j,j+8):
                # 맨 왼쪽 위가 'W'라고 할때
                if k % 2 == 0:
                    if l % 2 == 0:
                        if board[k][l] == "B":
                            re_1 += 1
                    else:
                        if board[k][l] == "W":
                            re_1 += 1
                else:
                    if l % 2 == 0:
                        if board[k][l] == 'W':
                            re_1 += 1
                    else:
                        if board[k][l] == 'B':
                            re_1 += 1
                
                # 맨 왼쪽 위가 'B'라고 할때
                if k % 2 == 0:
                    if l % 2 == 0:
                        if board[k][l] == "W":
                            re_2 += 1
                    else:
                        if board[k][l] == "B":
                            re_2 += 1
                else:
                    if l % 2 == 0:
                        if board[k][l] == 'B':
                            re_2 += 1
                    else:
                        if board[k][l] == 'W':
                            re_2 += 1
        result.append(re_1)
        result.append(re_2)

result.sort()
print(result[0])