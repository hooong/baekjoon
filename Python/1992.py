# 압축이 가능한지 확인
def comp(n,startX,startY):
    global result
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
        result += str(color)
    else:
        # 4분할할때마다 괄호를 열고 닫음.
        result += '('
        comp(n//2, startX, startY)
        comp(n//2, startX, startY + n//2)
        comp(n//2, startX + n//2, startY)
        comp(n//2, startX + n//2, startY + n//2)
        result += ')'

n = int(input())
paper = [list(input()) for _ in range(n)]

result = ''

comp(n,0,0)

print(result)


