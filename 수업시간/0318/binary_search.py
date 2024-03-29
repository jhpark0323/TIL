# 이진 탐색
arr = [324, 32, 22114, 16, 48, 93, 422, 21, 316]

# 1. 정렬된 상태의 데이터
arr.sort()
print(arr)

# 2. 이진 탐색 -> 반복문 ver
def binary_search(target):
    # 제일 왼쪼, 오른쪽 index 구하기
    low = 0
    high = len(arr)-1
    # 탐색횟수
    cnt = 0

    # 해당 숫자를 찾으면 종료
    # 더이상 쪼갤 수 없을 때까지
    while low <= high:
        mid = (low + high) // 2
        cnt += 1

        # 가운데 숫자가 정답이면 종료
        if arr[mid] == target:
            return mid, cnt

        elif arr[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    # 못찾으면 -1 반환
    return -1, cnt

print(f'21 = {binary_search(21)}')
print(f'324 = {binary_search(324)}')
print(f'888 = {binary_search(888)}')



# 3. 이진 탐색 -> 재귀함수 ver
def binary_search_recursion(low, high, target):
    # 기저 조건(언제까지 재귀가 반복되어야 할까?
    if low > high:
        return -1

    # 다음 재귀 들어가기 전엔 무엇을 해야할까?
    # 정답 판별
    mid = (low + high) // 2
    if target == arr[mid]:
        return mid

    # 다음 재귀 함수 호출 (파라미터 생각 잘하기!)
    if target < arr[mid]:
        return binary_search_recursion(low, mid-1, target)

    else:
        return binary_search_recursion(mid+1, high, target)

    # 재귀 함수에서 돌아왔을때 어떤작업을 해야 할까?
    # 여기서는 없음

print(f'21 = {binary_search_recursion(0, len(arr), 21)}')
print(f'324 = {binary_search_recursion(0, len(arr), 324)}')
print(f'888 = {binary_search_recursion(0, len(arr), 888)}')