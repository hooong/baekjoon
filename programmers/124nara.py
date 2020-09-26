# 124 나라의 숫자

def solution(n):
    if n == 0:
        return ''
        
    if n % 3 == 0:
        return solution(n//3 - 1) + '4'
    else:
        return solution(n//3) + str(n%3)


if __name__ == '__main__':
    print(solution(4))
