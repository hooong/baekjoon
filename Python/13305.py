# 13305번 주유소

n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

total_price = 0
i = 0
while i < len(price)-1:
    cur_price = price[i]
    fuel = 0
    j = i
    while True:
        if j == len(price)-1:
            break

        if cur_price <= price[j]:
            fuel += length[j]
            j += 1
        else:
            break
    total_price += (fuel * cur_price)
    i = j

print(total_price)
