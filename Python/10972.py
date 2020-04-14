# 10972번 다음 순열
import sys

# main
n = int(input())
seq = [int(x) for x in sys.stdin.readline().split()]

k = -1
# 1. k의 최댓값 구하기
for i in range(len(seq)-1):
    if seq[i] < seq[i+1]:
        k = i

if k == -1:     # 내림차순인 경우 
    print(-1)
else:
    # 2. l의 최댓값 구하기
    for j in range(k+1,len(seq)):
        if seq[k] < seq[j]:
            l = j
    
    # 3. k와 l의 값 바꿔치기
    seq[k], seq[l] = seq[l], seq[k]

    # 4. k 이후 정렬
    tmp = seq[k+1:]
    tmp.sort()
    answer = seq[:k+1] + tmp

    for num in answer:
        print(num, end=' ')
    print()
