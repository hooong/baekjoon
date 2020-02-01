# 잘린 부분이 모두 한 숫자인지 확인
def isOne(n,startX,startY):
    is_same = True
    color = paper[startX][startY]

    for i in range(startX,startX+n):
        for j in range(startY,startY+n):
            if color != paper[i][j]:
                is_same = False
                break
        if not is_same:
            break

    if is_same:
        incre_cnt(color)
    else:
        # 9분할 과정
        isOne(n//3, startX, startY)
        isOne(n//3, startX, startY + n//3)
        isOne(n//3, startX, startY + (n//3)*2)
        isOne(n//3, startX + n//3, startY)
        isOne(n//3, startX + n//3, startY + n//3)
        isOne(n//3, startX + n//3, startY + (n//3)*2)
        isOne(n//3, startX + (n//3)*2, startY)
        isOne(n//3, startX + (n//3)*2, startY + n//3)
        isOne(n//3, startX + (n//3)*2, startY + (n//3)*2)

def incre_cnt(color):
    global cnt_minus, cnt_zero, cnt_one
    if color == -1:
        cnt_minus += 1
    elif color == 0:
        cnt_zero += 1
    else:
        cnt_one += 1

n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]

cnt_minus = 0
cnt_zero = 0
cnt_one = 0

isOne(n,0,0)

print(cnt_minus)
print(cnt_zero)
print(cnt_one)


