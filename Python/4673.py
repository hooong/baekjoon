a = set()
for i in range(10000):
    b = str(i)
    result = i
    for j in b:
        result += int(j)
    a.add(result)

for i in range(10000):
    if i not in a:
        print(i)