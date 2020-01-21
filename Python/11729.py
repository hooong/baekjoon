# 하노이탑
def hanoi(n,from_pos,tmp_pos,to_pos):
    # 1이면 하나만 옮기면 된다.
    if n == 1:
        result.append([from_pos,to_pos])
        return

    hanoi(n-1,from_pos,to_pos,tmp_pos)  # n-1개를 from_pos에서 tmp_pos으로 옮김
    result.append([from_pos,to_pos])    # 맨 밑에 한개를 from에서 to로 옮김
    hanoi(n-1,tmp_pos,from_pos,to_pos)  # 다시 tmp에 있는 n-1개를 to로 옮김


result = []
num = int(input())

hanoi(num,1,2,3)

print(len(result))
for i in result:
    print(i[0],i[1])