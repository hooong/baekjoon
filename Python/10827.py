# 10827번 a^b

a, b = input().split()
b = int(b)

post_dot = (len(a) - 1) - a.index('.')
a = a.replace('.', '')
pos_dot = post_dot * b

a = str(pow(int(a), b))
if len(a) > pos_dot:
    ans = ''
    for i in range(len(a)):
        if i == (len(a) - pos_dot):
            ans += '.'
        ans += a[i]
else:
    ans = '0.'
    for i in range(pos_dot - len(a)):
        ans += '0'
    ans += a

print(ans)

