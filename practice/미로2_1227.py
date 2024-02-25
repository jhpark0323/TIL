dij = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dfs(row, col):
    visited = [[False] * 100 for _ in range(100)]
    visited[row][col] = True
    stack = [[row, col]]

    while stack:
        current_row, current_col = stack.pop()
        for neighbor in range(4):
            next_row, next_col = current_row+dij[neighbor][0], current_col+dij[neighbor][1]
            if 0 <= next_row < 100 and 0 <= next_col < 100 and miro[next_row][next_col] == '3':
                return 1

            if 0 <= next_row < 100 and 0 <= next_col < 100 and not visited[next_row][next_col] and miro[next_row][next_col] == '0':
                visited[next_row][next_col] = True
                stack.append([next_row, next_col])
    return 0

for test_case in range(1, 11):
    tc = int(input())
    miro = [list(input()) for _ in range(100)]
    # print(miro)
    row, col = -1, -1
    # 시작점 찾기
    for i in range(100):
        for j in range(100):
            if miro[i][j] == '2':
                row, col = i, j
                answer = dfs(row, col)
                break
        if row != -1:
            break

    print(f'#{test_case} {answer}')