# 메모리에러!!
# T = int(input())
# calendar = {}
# result = []

# for _ in range(T):
#     M, N, x, y = map(int, input().split())
    
#     i = 0
#     j = 0
#     count = 1
#     c = 0

#     while True:
#         i += 1
#         j += 1

#         if i > M:
#             i = 1
#         if j > N:
#             j = 1

#         calendar[count] = [i,j]
#         count += 1

#         if i == M and j == N:
#             break

#     key = list(calendar.keys())

    
#     for i in calendar:
#         c += 1
#         if calendar[i] == [x,y]:
#             result.append(i)
#             break
#         elif c == len(key):
#             result.append(-1)

# for i in result:
#     print(i)

def gcd(a, b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

def lcm(a, b):
    return a*b // gcd(a,b)

T = int(input())
result = []

for _ in range(T):
    M, N, x, y = map(int, input().split())

    count = x
    while True:
        if y == x:
            result.append(x)
            break
        elif count > lcm(M,N):
            result.append(-1)
            break
        elif y == (x+M) % N:
            count += M
            result.append(count)
            break
        else:
            count += M
            x = (x+M) % N

for i in result:
    print(i)