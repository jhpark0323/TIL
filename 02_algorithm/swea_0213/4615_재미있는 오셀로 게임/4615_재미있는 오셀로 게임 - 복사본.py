import sys
sys.stdin = open('sample_input(1).txt')

import pprint

def change(board, x, y, n):
    dx_col = [1, 1, 0, -1, -1, -1, 0, 1]
    dy_row = [0, 1, 1, 1, 0, -1, -1, -1]

    if board[y][x] == 1:
        for i in range(8):
            row = y + dy_row[i]
            col = x + dx_col[i]
            stack = []

            while 0 <= row < n and 0 <= col < n:
                if board[row][col] == 0:
                    break
                if board[row][col] == 2:
                    stack.append([row, col])
                elif board[row][col] == 1:
                    while stack:
                        row, col = stack.pop()
                        board[row][col] = 1
                    break
                row += dy_row[i]
                col += dx_col[i]

    if board[y][x] == 2:
        for i in range(8):
            row = y + dy_row[i]
            col = x + dx_col[i]
            stack = []

            while 0 <= row < n and 0 <= col < n:
                if board[row][col] == 0:
                    break
                if board[row][col] == 1:
                    stack.append([row, col])
                elif board[row][col] == 2:
                    while stack:
                        row, col = stack.pop()
                        board[row][col] = 2
                    break
                row += dy_row[i]
                col += dx_col[i]

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
        # change함수에 board와 돌을 놓은 좌표를 넣어 board판을 update함
        board = change(board, x, y, n)

    pprint.pprint(board)