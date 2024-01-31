import sys
sys.stdin = open('input.txt')

import pprint
pp = pprint.PrettyPrinter(indent=4)

T = int(input())

for test_case in range(1, T+1):

    n, k = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(n)]

    # pp.pprint(puzzle)
    total = 0

    # 세로기준
    # 행의 갯수만큼 순회
    for row in range(n-k+1):
        # 열의 갯수만큼 순회
        for col in range(n):
            t_f_length = 0
            # t_f에 1씩 더해서 k이면 k자리 이상의 글자가 들어갈 수 있음
            for i in range(k):
                if puzzle[row+i][col] == 1:
                   t_f_length += 1
            # 다 더했을 때 k이면 뒤에 또 1이있는지 검사, 이때 범위안에 들어가는지 체크
            if (t_f_length == k) & (row+k == n):  # 다 더했을 때 k이고, 그 뒤는 벽일때
                if row-1 == -1:  # 앞에도 벽일 때
                  total += 1
                elif row-1 >= 0:  # 앞에는 벽이 아닐때
                    if puzzle[row-1][col] == 0:
                        total += 1
            elif (t_f_length == k) & (row+k < n):  # 다 더했을 때 k이고, 그 뒤가 벽이 아닐 때
                if puzzle[row+k][col] == 0:  # 그 뒤가 0이고
                    if row - 1 == -1:  # 앞에도 벽일 때
                        total += 1
                    elif row - 1 >= 0:  # 앞에는 벽이 아닐때
                        if puzzle[row - 1][col] == 0:
                            total += 1

    # 가로기준
    # 행의 갯수만큼 순회
    for row in range(n):
        # 열의 갯수만큼 순회
        for col in range(n-k+1):
            t_f_width = 0
            # t_f에 1씩 더해서 k이면 k자리 이상의 글자가 들어갈 수 있음
            for i in range(k):
                if puzzle[row][col+i] == 1:
                    t_f_width += 1
            # 다 더했을 때 k이면 뒤에 또 1이있는지 검사, 이때 범위안에 들어가는지 체크
            if (t_f_width == k) & (col + k == n):  # 다 더했을 때 k이고, 그 뒤는 벽일때
                if col - 1 == -1:  # 앞에도 벽일 때
                    total += 1
                elif col - 1 >= 0:  # 앞에는 벽이 아닐때
                    if puzzle[row - 1][col] == 0:
                        total += 1
            elif (t_f_width == k) & (col + k < n):  # 다 더했을 때 k이고, 그 뒤는 벽이 아닐때
                if puzzle[row][col+k] == 0:  # 그 뒤가 0이고
                    if col - 1 == -1:  # 앞에도 벽일 때
                        total += 1
                    elif col - 1 >= 0:  # 앞에는 벽이 아닐때
                        if puzzle[row][col-1] == 0:
                            total += 1


    print(total)