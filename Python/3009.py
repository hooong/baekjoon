x = []
y = []

for _ in range(3):                      # 세 점 입력을 받음
    a, b = map(int, input().split())

    # 직사각형이므로 같은 좌표값이 x와 y에서 각각 2개씩 있으면 됨.
    if not a in x:                      # 없으면 일단 list에 넣음.             
        x.append(a)
    else:                               # 이미 list에 있으면 list에 있는 값 삭제
        x.remove(a)

    if not b in y:
        y.append(b)
    else:
        y.remove(b)
# 이렇게 하면 세번 모두 돌고 나면 무조건 하나씩 남는다.

print(x[0],y[0])