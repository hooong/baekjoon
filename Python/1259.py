# 1259번 팰린드롬수

# main
while True:
    n = input()

    if n == '0':
        break

    if n == n[::-1]:
        print('yes')
    else:
        print('no')
