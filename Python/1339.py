# 1339번 단어 수학
import sys, copy

# main
n = int(input())

words = []
alpha = [0 for _ in range(26)]
for _ in range(n):
    words.append(list(sys.stdin.readline().strip()))

for word in words:
    i = 1
    while word:
        alpha[ord(word.pop()) - 65] += i
        i *= 10

nums = []
for a in alpha:
    if not a == 0:
        nums.append(a)

nums.sort(reverse=True)

answer = 0
v = 9
for num in nums:
    answer += (v * num)
    v -= 1

print(answer)
