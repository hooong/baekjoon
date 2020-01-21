import sys

n = int(sys.stdin.readline())

nums = []
for _ in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)

nums.sort()

# 산술평균(arithmetic mean)
def arith_mean(nums):
    all_sum = sum(nums)
    mean = all_sum / len(nums)

    return round(mean,0)    # 반올림(소수첫째자리)

# 중앙값(median)
def median(nums):
    m = len(nums)//2

    return nums[m]

# 최빈값(mode)
def mode(nums):
    nums_dic = {}
    for num in nums:
        if num in nums_dic:
            nums_dic[num] += 1
        else:
            nums_dic[num] = 1
    
    # 빈도수가 같으면 같은것중에서 두번째로 작은 값 출력
    dic_value = list(nums_dic.values())
    dic_value.sort()
    max_value = dic_value[-1]

    mode_dics = []
    for num in list(nums_dic.keys()):
        if nums_dic[num] == max_value:
            mode_dics.append(num)

    if len(mode_dics) > 1:
        mode_dics.sort()
        return mode_dics[1]
    else:
        return mode_dics[0]

# 범위(scope)
def scope(nums):
    s = nums[-1] - nums[0]
    return s

print(int(arith_mean(nums)))
print(median(nums))
print(mode(nums))
print(scope(nums))
