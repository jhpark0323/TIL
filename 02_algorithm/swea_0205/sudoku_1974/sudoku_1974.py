import sys
sys.stdin = open('input.txt')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 스도쿠 배열 받기
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
    # print(sudoku)

    sum = 0
    # 각 row 확인
    for i in sudoku:
        sudoku_row = set(i)
        #   print(sudoku_row)
        if len(sudoku_row) != 9:
            sum += 1
    # print(sum)

    # 각 col 확인
    for idx in range(9):
        sudoku_col = 0
        for row in range(9):
            sudoku_col += sudoku[row][idx]
            # print(sudoku_col)
        if sudoku_col != 45:
            sum += 1
    # print(sum)

    # 각 3x3 행렬 확인
    for row in range(0, 9, 3):
        thr = 0
        for _ in range(3):
            for col in range(3):
                thr += sudoku[row][col]
                # print(sudoku[row][col])
                if col == 2:
                    row += 1
        if thr != 45:
            sum += 1
    if sum != 0:
        print(f'#{test_case} 0')
    elif sum == 0:
        print(f'#{test_case} 1')
