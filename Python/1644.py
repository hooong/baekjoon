# 1644번 소수의 연속합


# 에라토스테네스의 채
def eratos(n):
    nums = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if nums[i]:
            for j in range(i+i, n+1, i):
                nums[j] = False

    return [i for i in range(2, n+1) if nums[i]]

n = int(input())
answer = 0

primes = eratos(4000000)

tmp = primes[0]
i = j = 0
while i <= j:
    if tmp < n:
        if j + 1 <= len(primes) - 1:
            j += 1
            tmp += primes[j]
        else:
            tmp -= primes[i]
            i += 1
    elif tmp > n:
        tmp -= primes[i]
        i += 1
    else:
        answer += 1
        j += 1
        tmp += primes[j]
print(answer)
