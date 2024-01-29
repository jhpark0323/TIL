import sys
sys.stdin = open('input.txt')

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    testcase = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    # 행들의 합
    sum_row = []
    # 열들의 합
    sum_col = []

    for i in range(100):
        # 각 행의 합을 sum_row에 append
        sum_row.append(sum(arr[i]))

        # 빈 col list 생성
        col = []

        for j in range(100):
            # col에 arr[j]의 i번째 원소 append
            col.append(arr[j][i])
        # 반복문이 돌고 난 후 col의 합 sum_col에 append
        sum_col.append(sum(col))

    bottom_right = 0
    top_right = 0

    for i in range(100):
        bottom_right += arr[i][i]
        top_right += arr[99-i][i]

    # maximum = sum_row + sum_col + [bottom_right] + [top_right]
    maximum = max(max(sum_row), max(sum_col), bottom_right, top_right)
    print(f'#{testcase} {maximum}')