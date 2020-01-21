import sys

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
        else:   # 만약에 두번째 수가 같다면 첫번째 수로 비교를 해서 작은 것을 먼저 넣어줌.
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

n = int(sys.stdin.readline())

dots = []
for _ in range(n):
    a, b = map(int,sys.stdin.readline().split())
    dots.append([a,b])

# merge sort
dots = merge_sort(dots)

for dot in dots:
    print(dot[0],dot[1])