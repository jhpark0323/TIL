import sys
sys.stdin = open('sample_input(1).txt')

import pprint

def change(board, x, y, n):
    # 우 하 좌 상 순서 + 각각의 대각선 사이사이에 분포
    dx_col = [1, 1, 0, -1, -1, -1, 0, 1]
    dy_row = [0, 1, 1, 1, 0, -1, -1, -1]

    # 놓은 돌이 검은색(1)일 때
    if board[y][x] == 1:
        # delta 갯수
        for i in range(8):
            # stack에 한 줄로 있는 좌표들을 append
            stack = []
            row = y
            col = x
            while 1:
                # row에 delta방향으로 한칸씩 늘림
                row += dy_row[i]
                col += dx_col[i]
                # 한칸늘렸을 때 board에 없으면 break
                if not 0 <= row < n or not 0 <= col < n:
                    break
                # 한칸 더 갔을 때 흰색이 나오면 일단 stack에 append하고 넘어감
                if board[row][col] == 2:
                    stack.append([row, col])

                # 한칸 더 갔을 때 검은색이 나오면 pop으로 하나씩 빼서 흰색부분 검은색으로 칠함
                elif board[row][col] == 1:
                    # stack이 채워져 있으면
                    while stack:
                        # pop으로 빼서 row와 col을 구함
                        row, col = stack.pop()
                        # 검은색으로 바꿈
                        board[row][col] = 1
                    # 검은색이 나오면 delta 한 방향 끝
                    break

                # 만약 다음칸이 0이면 그냥 나옴
                elif board[row][col] == 0:
                    break

    # 놓은 돌이 흰색(2)일 때
    if board[y][x] == 2:
        # delta 갯수
        for i in range(8):
            # stack에 한 줄로 있는 좌표들을 append
            stack = []
            row = y
            col = x
            while 1:
                # row에 delta방향으로 한칸씩 늘림
                row += dy_row[i]
                col += dx_col[i]
                # 한칸늘렸을 때 board에 없으면 break
                if not 0 <= row < n or not 0 <= col < n:
                    break
                # 한칸 더 갔을 때 검은색이 나오면 일단 stack에 append하고 넘어감
                if board[row][col] == 1:
                    stack.append([row, col])

                # 한칸 더 갔을 때 흰색이 나오면 pop으로 하나씩 빼서 흰색부분 검은색으로 칠함
                elif board[row][col] == 2:
                    # stack이 채워져 있으면
                    while stack:
                        # pop으로 빼서 row와 col을 구함
                        row, col = stack.pop()
                        # 흰색으로 바꿈
                        board[row][col] = 2

                    # 검은색이 나오면 delta 한 방향 끝
                    break

                # 만약 다음칸이 0이면 그냥 나옴
                elif board[row][col] == 0:
                    break
    # print(board)
    return board

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())

    ls = [list(map(int, input().split())) for _ in range(m)]
    # print(ls)

    # 빈 보드판 생성
    board = [[0] * n for _ in range(n)]
    # print(board)

    # 보드판 세팅
    center = n // 2
    board[center-1][center-1] = 2
    board[center][center] = 2
    board[center-1][center] = 1
    board[center][center-1] = 1
    # pprint.pprint(board)

    for i in range(m):
        x, y = ls[i][0]-1, ls[i][1]-1
        board[y][x] = ls[i][2]
        # change함수에 board와 돌을 놓은 좌표를 넣어 board판을 update함
        board = change(board, x, y, n)
        # pprint.pprint(board)

    # pprint.pprint(board)

    black = 0
    white = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print(f'#{test_case} {black} {white}')