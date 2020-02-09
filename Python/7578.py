# 7578번 공장
from math import *
import sys

# 선을 그려 방문 업데이트
def update(node, start, end, idx):
    if idx < start or end < idx:
        return 0

    if start == end:
        tree[node] = 1
        return tree[node]

    mid = (start + end) // 2
    update(node*2,start,mid,idx)
    update(node*2+1,mid+1,end,idx)
    tree[node] = tree[node*2] + tree[node*2+1]
    return tree[node]
    

# 구간합 쿼리
def query(node, start, end, left, right):
    if right < start or end < left:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    return query(node*2,start,mid,left,right) + query(node*2+1,mid+1,end,left,right)

# main
n = int(sys.stdin.readline())
arrA = sys.stdin.readline().split()

# arrB dict 초기화
idx = 0
arrB = {}
for num in sys.stdin.readline().split():
   arrB[num] = idx
   idx += 1

# 세그먼트 트리
h = int(ceil(log2(n)))
t_size = 1 << (h+1)

tree = [0] * t_size

answer = 0
for num in arrA:
    s_idx = arrB[num]
    answer += query(1,0,n-1,s_idx,n-1)

    update(1,0,n-1,s_idx)

print(answer)
