n = int(input())
result = []

for _ in range(n):
    h, w, k = map(int, input().split())

    floor = k % h                                       # 층 수를 구함
    if floor == 0:                                      # 나머지가 0이면 꼭대기층
        floor = h
    number = (k-1) // h + 1                             # (k-1)을 높이로 나누고 1을 더하면 가로가 몇번째인지

    if number < 10:                                     # number가 10보다 작으면 가운데 0을 붙여줘야 호수가 완성됨
        result.append(str(floor)+'0'+str(number))
    else:
        result.append(str(floor)+str(number))

for i in result:
    print(i)