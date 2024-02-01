import sys
sys.stdin = open('input.txt')

import pprint

'''
어케 할까요?
1번방법
nxn행렬을 만드는데 그 주위를 -2로 감싼다
그리고 출발해서 가는 방향에 -1이 아닌 수가 있으면 회전한다. -> ㄱㅊ아 보이는데?

-> 난 먼가 1번으로 풀고 싶긴 함

2번방법
nxn행렬을 만들고 가는방향을 delta로 만들고? (아님 어떻게든) 4로 나눈 나머지에 맞는 방향으로 움직인다. 근데 그럼 언제 회전함?
'''


T = int(input())

for test_case in range(1, T+1):

    n = int(input())

    # arr = [[0] * n for _ in range(n)]

    # arr을 -2로 감싸고 nxn행렬에 -1을 넣어서 arr을 최종적으로 만듬
    # -1,-2를 쓴이유 : pprint할때 칸이 딱맞아서 이쁘게 보임!
    arr = [[-2] * (n+2)]
    for _ in range(n):
        arr.append([-2] + [-1] * n + [-2])
    arr.append([-2] * (n+2))

    # pprint.pprint(arr)

    # 우 하 좌 상 순서대로 만듬
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 방향을 잡아줄 변수
    direction = 0
    start_row = 1
    start_col = 1

    # 넣을 숫자의 갯수만큼 반복
    for i in range(1, n**2 + 1):
        # 1,1부터 시작해서 i를 arr에 넣음
        arr[start_row][start_col] = i

        # 시작지점의 행과 열에 delta만큼 움직여 주기
        start_row += di[direction]
        start_col += dj[direction]

        # 이런느낌으로 방향 전환
        if arr[start_row][start_col] != -1:
            # -2가 나오면 다시 원래대로 돌아와서 방향 틀기
            start_row -= di[direction]
            start_col -= dj[direction]
            # 방향틀기
            direction += 1
            direction = direction % 4
            # 튼 방향으로 한칸 전진
            start_row += di[direction]
            start_col += dj[direction]

    # arr완성!
    # pprint.pprint(arr)

    # 답을 낼 arr에서 -2들을 빼서 담을 answer_arr배열 생성
    answer_arr = [[0] * n for _ in range(n)]

    # 칸에 맞게 넣기
    for i in range(1, n+1):
        for j in range(1, n+1):
            answer_arr[i-1][j-1] = arr[i][j]

    # pprint.pprint((answer_arr))

    # 출력
    print(f'#{test_case}')
    for i in range(n):
        print(*answer_arr[i])