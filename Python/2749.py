# 2749번 피보나치 수 3

# 행렬 제곱
def mul(n,matrix1,matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000000

    return result

# 2분할
def devide(n,b,matrix):
    if b == 1:
        return matrix
    elif b == 2:
        return mul(n,matrix,matrix)
    else:
        tmp = devide(n,b//2,matrix)
        if b%2 == 0:
            return mul(n,tmp,tmp)
        else:
            return mul(n,mul(n,tmp,tmp),matrix)

# 입력
n = int(input())

# 기본 피보나치 행렬
fibo = [[0,1],
        [1,2]]
# 제곱 행렬
mul_mat = [[1,1],
           [1,2]]

# 제곱 수
b = n // 2

if b==0:
    print(fibo[0][n%2])
else:
    sq_mat = devide(2,b,mul_mat)
    result = mul(2,fibo,sq_mat)
    print(result[0][n%2] % 1000000)


