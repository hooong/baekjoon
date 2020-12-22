def KMP(s, p):
    global table

    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j-1]

        if s[i] == p[j]:
            if j == len(p)-1:
                print("find", end='')
                print(i - len(p) + 2)
                j = table[j]
            else:
                j += 1


def make_table(p):
    global table

    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j-1]

        if p[i] == p[j]:
            j += 1
            table[i] = j
    print(table)


if __name__ == "__main__":
    string = "abacdabacaabacaaba"
    pattern = "abcdabcdabc"

    table = [0] * len(pattern)
    make_table(pattern)

    KMP(string, pattern)
