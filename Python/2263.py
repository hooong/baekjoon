# 2263번 트리의 순회
import sys

sys.setrecursionlimit(10 ** 6)


def find_pre_order(l_in, r_in, l_post, r_post):
    if l_in > r_in or l_post > r_post:
        return

    parent = post_order[r_post]
    print(parent, end=' ')

    split_idx = idx[parent]
    left = split_idx - l_in

    find_pre_order(l_in, split_idx - 1, l_post, (l_post + left) - 1)
    find_pre_order(split_idx + 1, r_in, l_post + left, r_post - 1)


n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

idx = [0] * (n + 1)
for i in range(n):
    idx[in_order[i]] = i

find_pre_order(0, n - 1, 0, n - 1)
