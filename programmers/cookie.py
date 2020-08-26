from math import ceil, log2

def solution(cookie):
    answer = 0

    h = int(ceil(log2(len(cookie))))
    t_size = 1 << (h+1)
    tree = [0] * (t_size)

    init(1, 0, len(cookie)-1, cookie, tree)

    for i in range(len(cookie)-1):
        for j in range(1,len(cookie)):
            l = query(1, 0, len(cookie)-1, i, j)
            r = query(1, 0, len(cookie)-1, j+1, len(cookie)-1)

            if l==r:
                answer = max(answer, l)

    return answer

def init(node, start, end, cookie, tree):
    if start == end:
        tree[node] = cookie[start]
        return tree[node]
    
    mid = (start + end) // 2

    tree[node] = init(node*2, start, mid, cookie, tree) + init(node*2+1, mid+1, end, cookie, tree)
    return tree[node]

def query(node, start, end, left, right):
    if left > end or start > right:
        return 0

    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

if __name__ == '__main__':
    print(solution([1,1,2,3]))