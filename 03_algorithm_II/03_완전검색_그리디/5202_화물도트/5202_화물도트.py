import sys
sys.stdin = open('sample_input.txt')

'''
1. 종료시간을 기준으로 정렬
2. 다음 화물을 찾는데 시간 확인
'''

from collections import deque

T = int(input())

for test_case in range(1, T+1):
    # 신청서
    n = int(input())
    # arr[i][0] : 화물차의 작업 시작 시간, arr[i][1] : 종료 시간
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 종료시간을 기준으로 정렬
    arr.sort(key=lambda x: x[1])
    arr = deque(arr)
    # print(arr)

    # 처음 화물은 무조건 사용
    cnt = 1
    while arr:
        # 사용할 화물
        use = arr.popleft()
        # 다음 담을 수 있는 화물 찾기
        while arr:
            # 사용할 화물의 종료시간 보다 다음 화물의 시작시간이 더 크면 종료
            if use[1] <= arr[0][0]:
                cnt += 1
                break

            # 다음 들어있는 화물을 못쓰면 없앰
            arr.popleft()

    print(f'#{test_case} {cnt}')