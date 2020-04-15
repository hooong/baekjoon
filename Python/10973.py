# 10973번 이전 순열
import sys

# main
n = int(input())
seq = [int(x) for x in sys.stdin.readline().split()]

# 1. k의 최댓값 찾기
k = -1
for i in range(len(seq)-1):
    if seq[i] > seq[i+1]:
        k = i

if k == -1:     # 오름차순인 경우
    print(-1)
else:
    # 2. m의 최댓값 구하기
    for j in range(k+1,len(seq)):
        if seq[j] < seq[k]:
            m = j
    
    # 3. k와 m의 값 바꿔치기
    seq[k], seq[m] = seq[m], seq[k]

    # 4. k이후의 값들 내림차순으로 정렬
    tmp = seq[k+1:]
    tmp.sort(reverse=True)
    answer = seq[:k+1] + tmp

    for num in answer:
        print(num, end= ' ')
    print()
