cur_hour, cur_min = map(int, input().split(" "))
duration_time = int(input())

cur_time = cur_hour * 60 + cur_min
done_time = cur_time + duration_time

if done_time >= (24 * 60):
    done_time -= 24 * 60

print(done_time // 60, done_time % 60)
