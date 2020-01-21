import math as m

result = []

# 직각삼각형인지 판단하는 함수
def confirm_right(a,b,c):
    if (m.pow(a,2) + m.pow(b,2)) == m.pow(c,2):     # a^2 + b^2 = c^2
        result.append("right")
    else:
        result.append("wrong")

while True:
    a, b, c = map(int, input().split())

    if ( a == 0 ) and ( b == 0 ) and ( c == 0 ):
        break
    else:
        # a, b, c 중에서 가장 큰 수를 찾는다.
        if a > b:
            if a > c:
                confirm_right(b,c,a)
            else:
                confirm_right(a,b,c)
        else:
            if b > c:
                confirm_right(a,c,b)
            else:
                confirm_right(a,b,c)

for i in result:
    print(i)