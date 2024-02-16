import sys
sys.stdin = open('sample_input.txt')

from collections import deque

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(row, col):
    # 방문한 곳 표시
    visited = [[0] * (n) for _ in range(n)]
    # q에 좌표를 append
    q = deque([[row, col]])
    # print(q)

    # q가 빌 때 까지
    while q:
        # 현재 위치는 pop으로 꺼냄
        row, col = q.popleft()
        # 상하좌우 탐색
        for k in range(4):
            next_row = row + di[k]
            next_col = col + dj[k]
            # 범위안에 있고 방문하지 않았다면
            if 0 <= next_row < n and 0 <= next_col < n and not visited[next_row][next_col]:
                # 통로를 만나면
                if miro[next_row][next_col] == 0:
                    # 현재 위치의 횟수보다 1 증가
                    visited[next_row][next_col] = visited[row][col] + 1
                    q.append([next_row, next_col])

                # 도착지점을 만나면
                if miro[next_row][next_col] == 3:
                    # 그대로 본인 자리 return
                    return visited[row][col]

    # while문에서 return이 안나오면 도착 못한것이므로 0 return
    return 0


T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    miro = [list(map(int, list(input()))) for _ in range(n)]
    # print(miro)

    # answer의 초기값은 None
    answer = None

    for i in range(n):
        for j in range(n):
            # 출발지를 찾으면 함수에 대입
            if miro[i][j] == 2:
                answer = bfs(i, j)
                break
        # answer이 처음상태와 다르게 되면
        if answer != None:
            break

    print(f'#{test_case} {answer}')
