# 모노미노도미노

def green_simul(t, y):
    global green, green_top, score

    if t == 1:
        # 내려가는 상황
        green_top[y] += 1
        green[green_top[y]][y] = 1
    elif t == 2:
        tmp = max(green_top[y], green_top[y+1])
        green_top[y] = green_top[y+1] = tmp + 1
        green[green_top[y]][y] = 2
        green[green_top[y+1]][y+1] = -1
    else:
        # 내려가는 상황
        green_top[y] += 2
        green[green_top[y]-1][y] = 1
        green[green_top[y]][y] = 1

    # 터지는 상황
    ex_full = True
    while ex_full:
        ex_full = False
        for i in range(4):
            if green[i].count(0) == 0:
                score += 1
                ex_full = True
                green[i] = [0] * 4
        
        if ex_full:
            for i in range(6):
                for j in range(4):
                    if i == 0:
                        if green[i][j] in [1,2,-1]:
                            green_top[j] = i
                        else:
                            green_top[j] = -1
                    else:
                        if green[i][j] in [1,2]:
                            if not (i - 1 == green_top[j]):
                                if green[i][j] == 1:
                                        green[i][j] = 0
                                        green_top[j] += 1
                                        green[green_top[j]][j] = 1
                                elif green[i][j] == 2:
                                    tmp = max(green_top[j], green_top[j+1])
                                    green_top[j] = green_top[j+1] = tmp + 1
                                    green[i][j] = green[i][j+1] = 0
                                    green[green_top[j]][j] = 2
                                    green[green_top[j]][j+1] = -1
                            else:
                                green_top[j] = i                        

    # 범위 넘는 상황
    max_height = max(green_top)
    if max_height > 3:
        for _ in range(max_height-3):
            green.append([0] * 4)
            green.pop(0)
            for i in range(4):
                if green_top[i] >= 0:
                    green_top[i] -= 1


def blue_simul(t, x):
    global blue, blue_top, score

    if t == 1:
        # 내려가는 상황
        blue_top[x] += 1
        blue[blue_top[x]][x] = 1
    elif t == 2:
        # 내려가는 상황
        blue_top[x] += 2
        blue[blue_top[x]-1][x] = 1
        blue[blue_top[x]][x] = 1
    else:
        # 내려가는 상황
        tmp = max(blue_top[x], blue_top[x+1])
        blue_top[x] = blue_top[x+1] = tmp + 1
        blue[blue_top[x]][x] = 2
        blue[blue_top[x+1]][x+1] = -1

    # 터지는 상황
    ex_full = True
    while ex_full:
        ex_full = False
        for i in range(4):
            if blue[i].count(0) == 0:
                score += 1
                ex_full = True
                blue[i] = [0] * 4
        
        if ex_full:
            for i in range(6):
                for j in range(4):
                    if i == 0:
                        if blue[i][j] in [1,2,-1]:
                            blue_top[j] = i
                        else:
                            blue_top[j] = -1
                    else:
                        if blue[i][j] in [1,2]:
                            if not (i - 1 == blue_top[j]):
                                if blue[i][j] == 1:
                                        blue[i][j] = 0
                                        blue_top[j] += 1
                                        blue[blue_top[j]][j] = 1
                                elif blue[i][j] == 2:
                                    tmp = max(blue_top[j], blue_top[j+1])
                                    blue_top[j] = blue_top[j+1] = tmp + 1
                                    blue[i][j] = blue[i][j+1] = 0
                                    blue[blue_top[j]][j] = 2
                                    blue[blue_top[j]][j+1] = -1
                            else:
                                blue_top[j] = i

    # 범위 넘는 상황
    max_height = max(blue_top)
    if max_height > 3:
        for _ in range(max_height-3):
            blue.append([0] * 4)
            blue.pop(0)

            for i in range(4):
                if blue_top[i] >= 0:
                    blue_top[i] -= 1


n = int(input())
command = [list(map(int, input().split())) for _ in range(n)]

green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]
green_top = [-1] * 4
blue_top = [-1] * 4

score = 0
while command:
    t, x, y = command.pop(0)

    green_simul(t, y)
    blue_simul(t, x)

count = 0
for i in range(4):
    for j in range(4):
        if not green[i][j] == 0:
            count += 1
        if not blue[i][j] == 0:
            count += 1

print(score)
print(count)
