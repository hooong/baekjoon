def get_reward_two(num):
    return 1000 + num * 100


a, b, c = map(int, input().split(" "))

reward = 0
if a == b and b == c:
    reward = 10000 + a * 1000
elif a == b or b == c:
    reward = get_reward_two(b)
elif a == c:
    reward = get_reward_two(a)
else:
    reward = max(max(a, b), c) * 100

print(reward)
