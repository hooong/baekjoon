a, b = input().split()

a_rev = a[::-1]
b_rev = b[::-1]

result = a_rev if int(a_rev) > int(b_rev) else b_rev

print(result)