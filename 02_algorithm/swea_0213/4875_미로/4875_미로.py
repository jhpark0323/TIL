import sys
sys.stdin = open('sample_input.txt')

'''
1. 출발 위치를 찾는다.
2. 우 하 좌 상을 찾으며 위치를 옮긴다.
3. 이 때 옮긴 위치를 stack에 담는다.
4. 거기서 옮길수 있으면 다시 stack에 담고 더이상 못가면 pop을 해서 전단계로 간다.
5. 옮긴 후 원래있던 위치를 1로 바꿔야 다시 그 방향으로 안갈듯
'''

import pprint

# 상하좌우로 움직이는 함수
def find_way(row, col, miro, n):
    # 순서대로 우, 하, 좌, 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    current = [row, col]
    stack = [current]
    visited = [[0]*n for _ in range(n)]
    try:
        while 1:
            # 우 하 좌 상을 돌며 체크
            for i in range(4):
                # miro의 범위내에 있는지 확인
                if 0 <= current[0] + di[i] < n and 0 <= current[1] + dj[i] < n:
                    # 옮길 위치에 0(통로)가 있고 방문하지 않았으면 옮김
                    if miro[current[0] + di[i]][current[1] + dj[i]] == '3':
                        answer = 1
                        return answer

                    if miro[current[0] + di[i]][current[1] + dj[i]] != '1' and visited[current[0] + di[i]][current[1] + dj[i]] == 0:
                        # 현재위치의 visited를 1로 바꾸고 자리를 옮긴 후 stack에 담는다
                        visited[current[0] + di[i]][current[1] + dj[i]] = 1
                        current = [current[0] + di[i], current[1] + dj[i]]
                        stack.append(current)
                        break
                        # print(stack)
                        # row += di[i]
                        # col += dj[i]
            # 모든 방향을 다 돌았는데 0(통로)가 안나옴
            else:
                current = stack.pop()

            # 도착 지점에 다다르면 멈춤
            if miro[current[0]][current[1]] == '3':
                answer = 1
                return answer

    # 만약 다돌았는데도 도착지에 도착못하면 빈 stack을 pop하는 상황이 나옴 -> 그러면 except로 나옴
    except:
        answer = 0
        return answer


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    miro = [list(input()) for _ in range(n)]
    # pprint.pprint(miro)

    # 시작위치 찾기
    start_row = -1
    for i in range(n):
        for j in range(n):
            if miro[i][j] == '2':
                start_row, start_col = i, j
                break
        if start_row > 0:
            break

    # print(start_row, start_col, miro[start_row][start_col])

    print(f'#{test_case} {find_way(start_row, start_col, miro, n)}')