x = int(input())

i = 0
j = 1

while True:
    # 1,2,3,4순으로 개수가 늘어남.
    if x in range(j,j+i+1):
        x -= j                  # x번째 줄에서의 순서
        a = i-x                 # 행
        b = i-a                 # 열
        if (i+1)%2 == 0:        # 지그재그이므로 홀짝으로 순서구분
            print(b+1,'/',a+1, sep='')
        else:
            print(a+1,'/',b+1, sep='')
        break
    i += 1
    j += i