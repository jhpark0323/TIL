import sys
sys.stdin = open('input1.txt')

import pprint

T = int(input())

for test_case in range(1, T+1):

    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    # pprint.pprint(arr)

    # 꽃가루 ls
    pollen_ls = []

    # n행 순회
    for i in range(n):
        # m열 순회
        for j in range(m):
            # 꽃가루의 합 담을 변수
            pollen = 0

            pollen += arr[i][j]

            # 우측방향에서 arr이 있을 때
            if 0 <= j + 1 < m:
                pollen += arr[i][j+1]

            # 아래방향에서 arr이 있을 때
            if 0 <= i + 1 < n:
                pollen += arr[i+1][j]

            # 좌측방향에서 arr이 있을 때
            if 0 <= j - 1 < m:
                pollen += arr[i][j-1]

            # 위측방향에서 arr이 있을 때
            if 0 <= i - 1 < n:
                pollen += arr[i-1][j]

            pollen_ls.append(pollen)

    print(f'#{test_case} {max(pollen_ls)}')