# 1107번 리모컨
import sys

# 버튼으로 누를 수 있는지 확인
def check_click(ch):
    global btn

    str_ch = list(str(ch))

    for c in str_ch:
        if not btn[int(c)]:
            return False
    return True

# main
n = int(input())
m = int(input())

# 망가진 버튼
btn = [True for _ in range(10)]
nbtn = [int(x) for x in sys.stdin.readline().split()]
for b in nbtn:
    btn[b] = False

minClick = abs(n-100)

for ch in range(1000000):
    if check_click(ch):
        click = abs(ch-n) + len(str(ch))
        minClick = min(minClick, click)

print(minClick)