total_price = int(input())
n = int(input())

calc_price = 0
for _ in range(n):
    price, count = map(int, input().split(" "))
    calc_price += price * count

if total_price == calc_price:
    print("Yes")
else:
    print("No")
