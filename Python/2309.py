# 2309번 일곱 난쟁이

# find
def find(h):
    sumH = sum(h)

    for i in range(8):
        for j in range(i+1,9):
            tmp = sumH - h[i] - h[j]

            if tmp == 100:
                h.pop(j)
                h.pop(i)
                return h
            
# main
dwarf = []
for _ in range(9):
    dwarf.append(int(input()))

answer = find(dwarf)
answer.sort()

for i in answer:
    print(i)
            