# 2512번 예산

n = int(input())
budgets = list(map(int, input().split()))
total = int(input())

max_limit = 0
l = 0
r = total
while l <= r:
    mid = (l + r) // 2

    sub_total = 0
    for budget in budgets:
        if budget > mid:
            sub_total += mid
        else:
            sub_total += budget

    if sub_total > total:
        r = mid - 1
    else:
        max_limit = max(max_limit, mid)
        l = mid + 1

max_budget = max(budgets)
if max_budget > max_limit:
    print(max_limit)
else:
    print(max_budget)
