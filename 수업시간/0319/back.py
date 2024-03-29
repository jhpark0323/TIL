# 백트래킹
# 완전탐색 + 가지치기
# 가능성이 없는 경우의 수를 제거하는 기법

# 중복된 순열
# 1~3까지 숫자 배열이 있을 때
# 111, 112, 113, 121, 122, ..., 332, 333

# 재귀함수 -> 특정 시점으로 돌아오는게 핵심!
# 재귀함수 팁
# 파라미터 : 바로작성 X
# 구조를 먼저 잡으면 자연스럽게 필요한 변수들이 보임!

arr = [i for i in range(1, 4)]
path = [0] * 3

def dfs(level):
    # 기저 조건
    # 이 문제에서는 3개를 뽑았을 때 까지 반복
    if level == 3:
        print(*path)
        return

    # 들어가기 전
    # 다음 재귀 호출
    #   - 다음에 갈 수 있는 곳들은 어디인가?
    #   - 이 문제에서는 1,2,3 세가지 경우의 수(arr의 길이만큼)가 존재
    '''
    path[level] = 1
    dfs(level+1)

    path[level] = 2
    dfs(level+1)

    path[level] = 3
    dfs(level+1)    
    '''

    for i in range(len(arr)):
        path[level] = arr[i]
        dfs(level+1)

    # 갔다와서 할 로직

# dfs(0)


# 순열
# 123, 132, 213, 231, 312, 321
# 조건 : 숫자는 한번만 활용

arr = [i for i in range(1, 4)]
path = [0] * 3

def dfs_permu(level):
    # 기저 조건
    # 이 문제에서는 3개를 뽑았을 때 까지 반복
    if level == 3:
        print(*path)
        return

    # 들어가기 전
    # 다음 재귀 호출
    #   - 다음에 갈 수 있는 곳들은 어디인가?
    #   - 이 문제에서는 1,2,3 세가지 경우의 수(arr의 길이만큼)가 존재
    '''
    path[level] = 1
    dfs(level+1)

    path[level] = 2
    dfs(level+1)

    path[level] = 3
    dfs(level+1)    
    '''

    # 갈 수 있는 후보군

    for i in range(len(arr)):
        # 여기는 못가 (가지치기)

        # 백트래킹 코드 팁
        # 갈 수 없는 경우를 활용
        # 아래 코드 처럼 갈 수 없을 때 continue

        if arr[i] in path:
            continue

        path[level] = arr[i]
        dfs_permu(level+1)
        # 갔다와서 할 로직
        # 기존 방문을 초기화
        path[level] = 0

dfs_permu(0)