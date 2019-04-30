#점수를 담을 리스트
score = []

#다섯명의 점수 입력 후 40점 미만이면 40 저장.
for i in range(5):
    input_score = int(input())
    if input_score < 40:
        score.append(40)
    else:
        score.append(input_score)

#평균 출력
print(sum(score)//5)