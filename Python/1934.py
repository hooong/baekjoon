# 1934번 최소공배수

# main
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    mul = a * b

    # 최대공약수
    while True:
        if a == 0:
            gcd = b
            break

        tmp = a
        a = b % a
        b = tmp
    
    #최소공배수
    lcm = mul // gcd

    print(lcm)

