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
        if left[i] < right[j]:
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

ropes = []
for _ in range(n):
    ropes.append(int(input()))

# 큰것부터 차례로 정렬
ropes = merge_sort(ropes)

weights = []
for i in range(n):
    # 로프를 다 사용하지 않아도 되므로 큰것부터 차례로 따져보면 작을걸 기준으로 로프 개수만큼 곱해주면
    # 로프를 가지고 들 수 있는 중량이 나온다.
    weights.append(ropes[i]*(i+1))

# 그 중 최댓값을 출력해준다.
print(max(weights))
