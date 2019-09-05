pay = int(input())
pay = 1000 - pay

count = 0           # 동전의 개수
coins = [500,100,50,10,5,1]  # 잔돈의 단위
for coin in coins:      # 큰것부터 뺄수있는만큼씩 빼준다.
    if pay == 0:
        break
    while pay >= coin:
        pay -= coin
        count += 1

print(count)