# 10819번 차이를 최대로
import sys

# 다음 순열 찾는 함수
def nextseq(s):
    k = -1
    for i in range(len(s)-1):
        if s[i] < s[i+1]:
            k = i
    
    if k == -1:
        return -1

    for j in range(k+1,len(s)):
        if s[j] > s[k]:
            m = j
    
    s[k], s[m] = s[m], s[k]
    tmp = s[k+1:]
    tmp.sort()
    
    return s[:k+1] + tmp

# main
n = int(input())
seq = [int(x) for x in sys.stdin.readline().split()]
seq.sort()      # 처음부터 탐색을 위해 오름차순 정렬

maxDis = 0
while True:
    sumDis = 0
    for i in range(len(seq)-1):
        sumDis += abs(seq[i+1] - seq[i])
    
    maxDis = max(maxDis, sumDis)

    seq = nextseq(seq)
    if seq == -1:
        break

print(maxDis)