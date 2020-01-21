# merge_sort => O(nlogn)
# merge_sort, radix_sort, bubble_sort, insert_sort => stable!
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    # 반으로 자름
    left = nums[:len(nums)//2]
    right = nums[len(nums)//2:]

    # 재귀를 통해 각 요소가 한 개가 될때까지 자름
    left = merge_sort(left)
    right = merge_sort(right)

    # merge를 한 list를 넘겨줌
    return merge(left,right)

def merge(left, right):
    # 정렬한 list를 담을 result
    result = []
    i = 0       # left index
    j = 0       # right index
    while True:
        # 두개를 비교해서 작은 값을 result에 삽입
        if left[i][0] > right[j][0]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
        
        # left는 끝나고 right는 끝나지 않았을 경우 남은거 다 삽입
        if i == len(left) and j < len(right):
            while True:
                if j == len(right):
                    break
                
                result.append(right[j])
                j += 1
        
        # right는 끝나고 left는 끝나지 않았을 경우 남은거 다 삽입
        if j == len(right) and i < len(left):
            while True:
                if i == len(left):
                    break

                result.append(left[i])
                i += 1
        
        # 다 끝났을 경우 result 반환
        if i == len(left) and j == len(right):
            return result

n = int(input())

accounts = []
for _ in range(n):
    a, b = input().split()
    accounts.append([int(a),b])

# merge sort
accounts = merge_sort(accounts)

for account in accounts:
    print(account[0],account[1])




# 시간초과
# bubble_sort를 사용해봤지만 시간초과 => 안정성이있는 또다른 merge_sort로 해결

# import sys

# n = int(sys.stdin.readline())

# accounts = []
# for _ in range(n):
#     a, b = input().split()
#     accounts.append([a,b])

# for i in range(n-1):
#     for j in range(n-i-1):
#         if int(accounts[j][0]) > int(accounts[j+1][0]):
#             tmp = accounts[j]
#             accounts[j] = accounts[j+1]
#             accounts[j+1] = tmp

# for account in accounts:
#     print(account[0],account[1])