# 10974번 모든 수열

# 순열 찾기
def find(bs):
    k = -1
    # 1. k의 최댓값 구하기
    for i in range(len(bs)-1):
        if bs[i] < bs[i+1]:
            k = i
    
    # 마지막
    if k == -1:
        return -1

    # 2. m의 최댓값 구하기
    for j in range(k+1,len(bs)):
        if bs[k] < bs[j]:
            m = j
    
    # 3. k와 m 바꿔치기
    bs[k], bs[m] = bs[m], bs[k]

    # 4. k 이후 오름차순으로 정렬
    tmp = bs[k+1:]
    tmp.sort()
    return bs[:k+1] + tmp

# print
def printSeq(s):
    for num in s:
        print(num, end=' ')
    print()

# main
n = int(input())

seq = [x for x in range(1,n+1)]

while True:
    printSeq(seq)
    seq = find(seq)

    if seq == -1:
        break
