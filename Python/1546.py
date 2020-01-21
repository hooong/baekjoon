n = int(input())
score = [int(s) for s in input().split()]

big = score[0]
result = 0

for i in score:
    if i > big:
        big = i

for i in range(n):
    # if score[i] != big:
    score[i] = score[i]/big*100
    result += score[i]
    
print("%0.2f" %(result/n))