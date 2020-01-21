n = int(input())

i = 0
b = 2

while True:
    b += 6*i
    if n == 1:
        print(1)
        break
    # 범위가 6*1, 6*2, 6*3 ... 이런식으로 증가한다.
    elif n in range(b,b+(6*(i+1))):
        print(i+2)
        break
    else:
        i += 1