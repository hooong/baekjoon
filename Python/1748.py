# 1748번 수 이어 쓰기 1

# main
n = int(input())

count = 0
for i in range(1,n+1):
    count += len(str(i))

print(count)