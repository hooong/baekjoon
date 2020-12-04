# 5639번 이진 검색 트리
import sys
sys.setrecursionlimit(10 ** 6)


def post_order(left, right):
    if left == right:
        return
    elif left == right - 1:
        print(pre_order[left])
        return

    parent = pre_order[left]

    split_idx = left + 1
    while split_idx < right and pre_order[split_idx] < parent:
        split_idx += 1

    # 왼쪽 노드
    post_order(left + 1, split_idx)
    # 오른족 노드
    post_order(split_idx, right)
    print(parent)


pre_order = []
while True:
    try:
        node = int(sys.stdin.readline())
        pre_order.append(node)
    except:
        break
post_order(0, len(pre_order))
