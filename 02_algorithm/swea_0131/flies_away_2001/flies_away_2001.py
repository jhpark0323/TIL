import sys
sys.stdin = open('input.txt')

import pprint
pp = pprint.PrettyPrinter(indent=4)

T = int(input())

for test_case in range(1, T+1):

    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    # pp.pprint(arr)

    # 각 행마다 n-m+1의 횟수만큼 돌릴수 있다.
    # ex) 5x5 배열, 2x2 크기의 파리채 -> 각 행당 4번의 횟수만큼 내리칠 수 있음
    times = n - m + 1

    # 최댓값을 할당할 max_total 생성
    max_total = 0

    # times만큼 row를 순회
    for row in range(times):
        # times만큼 col을 순회
        for col in range(times):
            # arr[row][col]을 기준으로 mxm안에 있는 모든 수를 total에 합침
            total = 0
            # m만큼 행을 순회
            for i in range(m):
                # m만큼 열을 순회
                for j in range(m):
                    # 순회 할 때 마다 total에 합침
                    total += arr[row + i][col + j]

            # 최댓값 갱신시 max_total에 재할당
            if max_total <= total:
                max_total = total

    print(f'#{test_case} {max_total}')