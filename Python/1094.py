# 1094번 막대기

# main
X = int(input())

if X == 64:
    print(1)
else:
    sticks = [64]

    while True:
        s = sticks.pop()

        sHalf = s // 2
        if sum(sticks) + sHalf == X:
            print(len(sticks) + 1)
            break
        elif sum(sticks) + sHalf > X:
            sticks.append(sHalf)
        else:
            for _ in range(2):
                sticks.append(sHalf)
