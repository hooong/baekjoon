# 잘린 부분이 모두 한 색깔인지 확인
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
        isOne(n//2, startX, startY)
        isOne(n//2, startX, startY + n//2)
        isOne(n//2, startX + n//2, startY)
        isOne(n//2, startX + n//2, startY + n//2)

def incre_cnt(color):
    global cnt_b, cnt_w
    if color == 1:
        cnt_b += 1
    else:
        cnt_w += 1

n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]

cnt_b = 0
cnt_w = 0

isOne(n,0,0)

print(cnt_w)
print(cnt_b)


