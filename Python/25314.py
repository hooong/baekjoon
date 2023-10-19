n = int(input())

answer = "long int"
for _ in range((n - 4) // 4):
    answer = "long " + answer

print(answer)
