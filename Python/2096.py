# 2096번 내려가기
import sys, copy

# main
N = int(input())

dpMin = []
dpMax = []
for n in range(N):
    line = [int(x) for x in sys.stdin.readline().split()]

    if n == 0:
        dpMax = copy.deepcopy(line)
        dpMin = copy.deepcopy(line)
    else:
        tmpMax = copy.deepcopy(dpMax)
        tmpMin = copy.deepcopy(dpMin)
        
        # 최댓값, 최솟값
        for i in range(3):
            if i == 0:
                dpMax[i] = line[i] + max(tmpMax[i], tmpMax[i+1])
                dpMin[i] = line[i] + min(tmpMin[i], tmpMin[i+1]) 
            elif i == 1:
                dpMax[i] = line[i] + max(tmpMax[i-1], max(tmpMax[i], tmpMax[i+1]))
                dpMin[i] = line[i] + min(tmpMin[i-1], min(tmpMin[i], tmpMin[i+1]))
            elif i == 2:
                dpMax[i] = line[i] + max(tmpMax[i-1], tmpMax[i])
                dpMin[i] = line[i] + min(tmpMin[i-1], tmpMin[i])

print(max(dpMax), min(dpMin))