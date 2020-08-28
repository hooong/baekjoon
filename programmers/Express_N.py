def solution(N, number):
    answer = -1

    count = [set() for _ in range(9)]

    for i in range(1,9):
        count[i].add(int(str(N)*i))

    for i in range(1,9):
        for j in range(1, i):
            for k in range(1, i):
                if j+k == i:
                    for a in count[j]:
                        for b in count[k]:
                            count[i].add(a+b)
                            count[i].add(a-b)
                            count[i].add(a*b)
                            if not b == 0:
                                count[i].add(a//b)
        if number in count[i]:
            answer = i
            break

    return answer

if __name__ == '__main__':
    print(solution(5,12))