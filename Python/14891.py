# 14892번 톱니바퀴

def exec(gear_num, dir):
    global gears, visited

    if gear_num == 1:
        if visited[gear_num] and not gears[gear_num-1][2] == gears[gear_num][6]:
            visited[gear_num] = False
            exec(2, dir * -1)
    elif gear_num == 2:
        if visited[gear_num-2] and not gears[gear_num-1][6] == gears[gear_num-2][2]:
            visited[gear_num-2] = False
            exec(1, dir * -1)

        if visited[gear_num] and not gears[gear_num-1][2] == gears[gear_num][6]:
            visited[gear_num] = False
            exec(3, dir * -1)
    elif gear_num == 3:
        if visited[gear_num-2] and not gears[gear_num-1][6] == gears[gear_num-2][2]:
            visited[gear_num-2] = False
            exec(2, dir * -1)
        
        if visited[gear_num] and not gears[gear_num-1][2] == gears[gear_num][6]:
            visited[gear_num] = False
            exec(4, dir * -1)
    elif gear_num == 4:
        if visited[gear_num-2] and not gears[gear_num-1][6] == gears[gear_num-2][2]:
            visited[gear_num-2] = False
            exec(3, dir * -1)

    spin(gear_num-1, dir)


def spin(gear, dir):
    global gears

    if dir == 1:
        gears[gear].insert(0, gears[gear].pop())
    else:
        gears[gear].append(gears[gear].pop(0))

gears = [list(input()) for _ in range(4)]

k = int(input())
commands = [list(map(int,input().split())) for _ in range(k)]

visited = []
for c in commands:
    visited = [True] * 4
    visited[c[0]-1] = False
    exec(c[0], c[1])

answer = 0
for i in range(4):
    answer += int(gears[i][0]) * (2 ** i)

print(answer)

