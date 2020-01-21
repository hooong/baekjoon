t = int(input())
result = []

for _ in range(t):
    a, b = map(int, input().split())
    result.append(a+b)

k = 1
for i in result:
    print("Case #"+str(k)+": "+str(i))
    k += 1