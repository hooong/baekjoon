a, b = input().split()

# 뒤집기
a_rev = a[::-1]
b_rev = b[::-1]

# 뒤집힌 수 비교하기
result = a_rev if int(a_rev) > int(b_rev) else b_rev

print(result)