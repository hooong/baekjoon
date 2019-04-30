a = int(input())
b = int(input())
c = int(input())

a = str(a*b*c)
dic = {}

for i in range(10):
    dic[str(i)] = 0

for i in a:
    dic[i] += 1

for i in range(10):
    print(dic[str(i)])