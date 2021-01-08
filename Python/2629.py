# 2629번 양팔저울


def possible_weight(cur_num, cur_weight):
    global dp

    if dp[cur_num][cur_weight]:
        return

    dp[cur_num][cur_weight] = True

    if cur_num >= num_weight:
        return

    possible_weight(cur_num + 1, cur_weight + weight[cur_num])
    possible_weight(cur_num + 1, abs(cur_weight - weight[cur_num]))
    possible_weight(cur_num + 1, cur_weight)


num_weight = int(input())
weight = list(map(int, input().split()))

num_marble = int(input())
marble = list(map(int, input().split()))

dp = [[False] * (30 * 500 + 1) for _ in range(31)]

possible_weight(0, 0)

for w in marble:
    if w > (30 * 500):
        print('N', end=' ')
    elif dp[num_weight][w]:
        print('Y', end=' ')
    else:
        print('N', end=' ')
print()
