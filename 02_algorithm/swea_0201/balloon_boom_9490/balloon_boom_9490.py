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

            # 가운데 있는 종이 꽃가루 개수만큼 반복
            for k in range(arr[i][j] + 1):

                # 우측방향에서 arr이 있을 때
                if 0 <= j + k < m:
                    pollen += arr[i][j+k]

                # 아래방향에서 arr이 있을 때
                if 0 <= i + k < n:
                    pollen += arr[i+k][j]

                # 좌측방향에서 arr이 있을 때
                if 0 <= j - k < m:
                    pollen += arr[i][j-k]

                # 위측방향에서 arr이 있을 때
                if 0 <= i - k < n:
                    pollen += arr[i-k][j]

                # 위쪽에서 총 4번의 arr[i][j]이 더해졌기 때문에 3번빼줌
            pollen -= 3 * arr[i][j]

            pollen_ls.append(pollen)
    # print(pollen_ls)

    print(f'#{test_case} {max(pollen_ls)}')