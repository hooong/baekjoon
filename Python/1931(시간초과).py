# O(nlogn)인 merge를 써도 시간초과 왜??


import sys

n = int(input())

present = 0     # 현재 시간을 나타내는 변수
count = 0       # 회의 개수 카운트

meetings = []
for _ in range(n):
    a,b = sys.stdin.readline().split()
    meetings.append([int(a),int(b)]) 

# 소요시간에 따라 정렬
# 그냥 정렬을 쓰면 시간초과가 나는듯  = >  merge_sort를 써보자.
# meetings.sort()
# merge_sort => O(nlogn)
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
        if left[i][1] > right[j][1]:
            result.append(right[j])
            j += 1
        elif left[i][1] < right[j][1]:
            result.append(left[i])
            i += 1
        else:
            if lft[i][0] > right[j][0]:
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

meetings = merge_sort(meetings)

for i in range(n):
    meeting = meetings.pop(0)
    if meeting[0] >= present:
        present = meeting[1]
        count += 1
    
print(count)