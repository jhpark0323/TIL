import sys
sys.stdin = open('input.txt')

import pprint
pp = pprint.PrettyPrinter(indent=4)

T = int(input())

for test_case in range(1, T+1):

    n, k = map(int, input().split())

    # puzzle에 input을 받는데 행렬의 겉을 0으로 감쌈 -> index걱정 안해도 될듯
    puzzle = [[0] * (n+2)]
    for _ in range(n):
        puzzle.append([0] + list(map(int, input().split())) + [0])
    puzzle.append([0] * (n+2))

    pp.pprint(puzzle)

    total = 0
    # 행을 하나의 문자열로 만들기
    for row_ls in puzzle:
        row = ''.join(map(str, row_ls))
        # print(row)
        word = '0' + '1' * k + '0'
        # print(word)
        if word in row:
            # count함수 쓸라했는데 중복하는거 체크 못해서 일일이 셈
            # row를 슬라이싱으로 잘라서 생기는 모든 경우를 word와 비교해서 같으면 total += 1
            for cnt in range(len(row) - len(word) + 1):
                if row[cnt:cnt + len(word)] == word:
                    total += 1
    # print(total)

    # 열을 하나의 문자열로 만들기위해 puzzle_transpose로 전치행렬로 만들어서 행으로 만든방법 그대로 쓸거임
    puzzle_transpose = [[0]*(n+2) for _ in range(n+2)]

    # 전치행렬 만들기
    for i in range(n+2):
        for j in range(n+2):
            puzzle_transpose[i][j] = puzzle[j][i]
    # pp.pprint(puzzle_transpose)

    # 열을 하나의 문자열로 만들기 -> 전치행렬을 이용해 행으로 만들기
    for row_ls in puzzle_transpose:
        row = ''.join(map(str, row_ls))
        # print(row)
        word = '0' + '1' * k + '0'
        # print(word)
        if word in row:
            # count함수 쓸라했는데 중복하는거 체크 못해서 일일이 셈
            # row를 슬라이싱으로 잘라서 생기는 모든 경우를 word와 비교해서 같으면 total += 1
            for cnt in range(len(row) - len(word) + 1):
                if row[cnt:cnt + len(word)] == word:
                    total += 1
    print(f'#{test_case} {total}')


# for cnt in range(len(row) - len(word) + 1):
#     if row[cnt:cnt+len(word)] == word:
#         total += 1

# word = '01110111011100' # 14
# w = '01110'  # 5
# print(word.count(w))
# print(len(word), len(w))