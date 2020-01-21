n = int(input())

tmp = []
score = []
m = []
p= []

for i in range(n):
    tmp = [int(s) for s in input().split()]
    m.append(tmp.pop(0))
    score += tmp

for i in range(n):
    result = []
    j = m.pop(0)
    for k in range(j):
        result.append(score.pop(0))
    avg = sum(result)/j
    c = 0
    for k in result:
        if avg < k:
            c += 1
    p.append(c/j*100)

for i in p:
    print("%0.3f"%i,'%', sep = '')