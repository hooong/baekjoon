# 11444번 피보나치 수 6

def mul(a, b):
    result = [[0] * 2 for _ in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000000007

    return result


n = int(input())
answer = [[1, 0], [0, 1]]
fib = [[1, 1], [1, 0]]

while n > 0:
    if n % 2 == 1:
        answer = mul(answer, fib)
    fib = mul(fib, fib)
    n //= 2

print(answer[0][1] % 1000000007)
