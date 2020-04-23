# 15829번 Hashing

# main
l = int(input())
s = input()
r = 31
m = 1234567891

rs = [1 for _ in range(51)]
for i in range(1,51):
    rs[i] = (rs[i-1] * r) % m

result = 0
for i in range(l):
    a = ord(s[i]) - ord('a') + 1
    result += (a * rs[i]) % m

print(result)
