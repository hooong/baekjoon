# 2168번 경찰차
import sys


def calc_dis(num, c_pos, n_pos):
    if num == 1:
        return abs(a_pos[c_pos][0] - a_pos[n_pos][0]) + abs(a_pos[c_pos][1] - a_pos[n_pos][1])
    else:
        return abs(b_pos[c_pos][0] - b_pos[n_pos][0]) + abs(b_pos[c_pos][1] - b_pos[n_pos][1])


def find_dp(a, b):
    global dp

    if a == w or b == w:
        return 0

    if not dp[a][b] == 0:
        return dp[a][b]

    n_pos = max(a, b) + 1

    # a 경찰차
    n_a = find_dp(n_pos, b) + calc_dis(1, a, n_pos)

    # b 경찰차
    n_b = find_dp(a, n_pos) + calc_dis(2, b, n_pos)

    dp[a][b] = min(n_a, n_b)
    return dp[a][b]


def find_path(a, b):
    if a == w or b == w:
        return

    n_pos = max(a, b) + 1

    n_a = dp[n_pos][b] + calc_dis(1, a, n_pos)
    n_b = dp[a][n_pos] + calc_dis(2, b, n_pos)

    if n_a > n_b:
        print(2)
        find_path(a, n_pos)
    else:
        print(1)
        find_path(n_pos, b)


n = int(sys.stdin.readline())
w = int(sys.stdin.readline())

a_pos = [(1, 1)]
b_pos = [(n, n)]
for _ in range(1, w+1):
    x, y = map(int, sys.stdin.readline().split())
    a_pos.append((x, y))
    b_pos.append((x, y))

# dp 및 최소거리 구하기
dp = [[0] * (w+1) for _ in range(w+1)]
print(find_dp(0, 0))

# 움직인 경찰차 추적
find_path(0, 0)

