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
        # 두개의 문자 길이를 비교
        if len(left[i]) > len(right[j]):
            result.append(right[j])
            j += 1
        elif len(left[i]) < len(right[j]):
            result.append(left[i])
            i += 1
        else:   # 길이가 같다면 사전순으로 str을 비교함
            if left[i] > right[j]:
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

words = []
for _ in range(n):
    # 뒤에 '\n'을 제거하고 line을 받아옴.
    word = sys.stdin.readline().strip('\n')
    # 중복을 없애줌.
    if not word in words:
        words.append(word)

# merge sort
words = merge_sort(words)

for word in words:
    print(word)