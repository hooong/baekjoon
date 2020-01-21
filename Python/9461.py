t = int(input())

ns = []
for _ in range(t):
    ns.append(int(input()))

for n in ns:
    if n == 1:
        print(1)
    elif n == 2:
        print(1)
    else:
        # 1,1,1,2,2,3,4,5,7,9,12...
        p = [0,1,1]
        for i in range(3,n+1):
            # P(n) = P(n-2) + P(n-3)
            p.append(p[i-2] + p[i-3])
        print(p[n])