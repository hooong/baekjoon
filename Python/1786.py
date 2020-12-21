# 1786번 찾기


def make_table(p):
    tmp = [0] * len(p)

    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = tmp[j-1]

        if p[i] == p[j]:
            j += 1
            tmp[i] = j

    return tmp


def KMP(s, p):
    cnt = 0
    pos = []

    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j-1]

        if s[i] == p[j]:
            if j == len(p)-1:
                cnt += 1
                pos.append(i - len(p) + 2)
                j = table[j]
            else:
                j += 1

    return cnt, pos


string = input()
pattern = input()

table = make_table(pattern)

answer, positions = KMP(string, pattern)
print(answer)
print(*positions)
