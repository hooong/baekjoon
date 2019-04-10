def han(n,c):
    if n < 100:
        c += 1
        return c
    a = str(n)
    b = True
    for i in range(len(a)):
        if i+2 == len(a):
            break
        if (int(a[i]) - int(a[i+1])) != (int(a[i+1]) - int(a[i+2])):
            b = False
    if b is True:
        c += 1
    return c

n = int(input())

c = 0
for i in range(1,n+1):
    c = han(i,c)

print(c)