# 2960번 에라토스테네스의 체

n, k = map(int, input().split())

eratos = [i for i in range(2, n+1)]

delete_nums = []
while eratos:
    delete_num = eratos.pop(0)
    delete_nums.append(delete_num)

    tmp = delete_num
    while tmp <= n:
        if tmp in eratos:
            eratos.remove(tmp)
            delete_nums.append(tmp)
        tmp += delete_num

print(delete_nums[k-1])
