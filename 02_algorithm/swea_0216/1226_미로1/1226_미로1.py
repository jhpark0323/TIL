import sys
sys.stdin = open('input.txt')

'''
이문제는 dfs가 더 나을듯?
'''

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(row, col):
    # 방문 행렬
    visited = [[False] * 16 for _ in range(16)]
    # 첫 위치 방문
    visited[row][col] = True
    # stack에는 행과 열 list를 넣어줌
    stack = [[row, col]]

    # stack이 빌 때 까지
    while stack:
        # 현재 위치의 행과 열은 stack에서 꺼냄
        row, col = stack.pop()
        # 4방향으로 움직임
        for dij in range(4):
            # 다음 방향의 row, col
            next_row = row + di[dij]
            next_col = col + dj[dij]

            # 범위안에 들어있고 방문하지 않은 곳이면
            if 0 <= next_row < 16 and 0 <= next_col < 16 and not visited[next_row][next_col]:
                # 다음 위치가 3이면 도착
                if miro[next_row][next_col] == 3:
                    return 1
                # 다음 위치가 0(통로)이면
                if miro[next_row][next_col] == 0:
                    # 방문 표시
                    visited[next_row][next_col] = True
                    # stack에 새로운 행과 열 append
                    stack.append([next_row, next_col])

    # while문이 다돌아도 3에 못도착했을 때
    return 0



import pprint

for test_case in range(10):
    tc = int(input())

    miro = [list(map(int, list(input()))) for _ in range(16)]

    # pprint.pprint(miro)

    answer = None

    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                answer = dfs(i, j)
                break

        if answer != None:
            break
    print(f'#{tc} {answer}')