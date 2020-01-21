#음계 입력
play = [int(i) for i in input().split()]

before = play[0]
count = 0

#판별하기
if play[0] == 1:
    for i in range(7):
        if (before+1) == play[i+1]:
            before += 1
            count += 1
            if count == 7:
                print("ascending")
        else:
            print("mixed")
            break
elif play[0] == 8:
    for i in range(7):
        if (before-1) == play[i+1]:
            before -= 1
            count += 1
            if count == 7:
                print("descending")
        else:
            print("mixed")
            break
else:
    print("mixed")
        
