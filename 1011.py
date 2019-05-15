n = int(input())
result = []

for _ in range(n):
    x, y = map(int, input().split())
    k = y - x                               # 두 점의 거리 계산 

    i = 1
    while True:
        if k == 1:
            result.append(1)                # 1일땐 1번
            break
        elif k == 2:
            result.append(2)                # 2일땐 2번
            break
        elif k in range(i*i-(i-1), i*i+1):  # i제곱과의 관계가 있다.
            result.append(2*i-1)
            break
        elif k in range(i*i+1, i*i+i+1):
            result.append(2*i)
            break
        else:
            i += 1

for i in result:
    print(i)

