# 2042번 구간 합 구하기
from math import *

# seg_tree init
def init(node, start, end):

    if start == end:
        tree[node] = arr[start]
        return tree[node]
    
    mid = (start + end) // 2

    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]

# 수의 변경
def update(node, i, diff, start, end):
    if not (start <= i and i <= end):
        return
    
    tree[node] += diff

    if start == end:
        return
    elif start != end:
        mid = (start + end) // 2
        update(node*2, i, diff, start, mid)
        update(node*2+1, i, diff, mid+1, end)

# 구간의 합 쿼리
def query(node, start, end, left, right):
    if left > end or start > right:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

# main
n, m, k = map(int,input().split())

h = int(ceil(log2(n)))
t_size = 1 << (h+1)

arr = []
tree = [0] * (t_size)

for _ in range(n):
    arr.append(int(input()))

init(1,0,n-1)

for _ in range(m+k):
    a, b, c = map(int,input().split())

    if a == 1:
        # update
        diff = c - arr[b-1]
        arr[b-1] = c
        update(1, b-1, diff, 0, n-1)

    elif a == 2:
        # query
        print(query(1, 0, n-1, b-1, c-1))