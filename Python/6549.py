# 6549번 히스토그램에서 가장 큰 직사각형
from math import *
import sys

# 트리 초기화
def init(node,start,end):
    if start == end:
        tree[node] = start
    else:
        mid = (start + end) // 2
        init(node*2,start,mid)
        init(node*2+1,mid+1,end)
        if histo[tree[node*2]] <= histo[tree[node*2+1]]:
            tree[node] = tree[node*2]
        else:
            tree[node] = tree[node*2+1]

# 쿼리
def query(histo,tree,node,start,end,left,right):
    if right < start or left > end:
        return -1
    
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    l_index = query(histo,tree,node*2,start,mid,left,right)
    r_index = query(histo,tree,node*2+1,mid+1,end,left,right)
    if l_index == -1:
        return r_index
    elif r_index == -1:
        return l_index
    else:
        if histo[l_index] < histo[r_index]:
            return l_index
        else:
            return r_index

# 최대 넓이 구하기
def getMaxArea(histo,tree,left,right):
    min_index = query(histo,tree,1,0,n-1,left,right)
    area = (right - left + 1) * histo[min_index]

    if left <= min_index-1:
        tmp_area = getMaxArea(histo,tree,left,min_index-1)
        if tmp_area > area:
            area = tmp_area
    if right >= min_index+1:
        tmp_area = getMaxArea(histo,tree,min_index+1,right)
        if tmp_area > area:
            area = tmp_area
    return area

# main
while True:
    histo = [int(x) for x in sys.stdin.readline().split()]
    if len(histo) <= 1:
        break
    else:
        n = histo.pop(0)

    h = int(ceil(log2(n)))
    t_size = 1 << (h+1)
    tree = [0] * t_size

    init(1,0,n-1)
    print(getMaxArea(histo,tree,0,n-1))
