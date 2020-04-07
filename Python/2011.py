# 2011번 암호코드

# main
code = input()

dp = [[0 for _ in range(2)] for _ in range(len(code)+1)]

# 첫째 한 자리
if int(code[0]) == 0:
    isError = True
else:
    dp[0][0] = 1    # 처음 두 자리로 가능할 경우를 위한 초기화
    dp[1][0] = 1    # 맨 앞으로 가능한 개수

# dinamic programming
for i in range(2, len(code)+1):
    # 암호가 잘 못 되었는지 확인.
    isOneErorr = False
    isTwoError = False
    
    # 한 자리 수의 경우
    if int(code[i-1]) > 0:
        dp[i][0] = sum(dp[i-1]) % 1000000
    else:
        isOneErorr = True

    # 두 자리 수의 경우
    if 10 <= int(code[i-2:i]) <= 26:
        dp[i][1] = sum(dp[i-2]) % 1000000
    else:
        isTwoError = True

    # 에러 발생
    if isOneErorr and isTwoError:
        break

print(sum(dp[-1]) % 1000000)
