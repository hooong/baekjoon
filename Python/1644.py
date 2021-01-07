# 1644번 소수의 연속합


# 에라토스테네스의 채
def eratos():
    nums = [False] * 4000001

    for i in range(2, 4000001):
        if not nums[i]:
            j = i + i
            while j < 4000001:
                nums[j] = True
                j += i

    primes = []
    for i in range(2, len(nums)):
        if not nums[i]:
            primes.append(i)

    return primes

n = int(input())

print(eratos())
