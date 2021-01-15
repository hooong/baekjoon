# 1032번 명령 프롬프트
import sys

n = int(sys.stdin.readline())
answer = ''

cmd = []
for _ in range(n):
    cmd.append(sys.stdin.readline().strip())

for i in range(len(cmd[0])):
    tmp = cmd[0][i]

    for j in range(1, n):
        if tmp != cmd[j][i]:
            answer += '?'
            break
    else:
        answer += tmp

print(answer if n != 1 else cmd[0])
