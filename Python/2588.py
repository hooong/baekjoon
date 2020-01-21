a = int(input())
b = input()

c = a * int(b[-1])
d = a * int(b[-2])
e = a * int(b[-3])

result = a * int(b)

print(c,d,e,result, sep="\n")