import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T+1):

    length = int(input())

    arr = [list(input()) for _ in range(8)]

    '''
    왼쪽상단의 좌표를 기준으로 lenght만큼의 길이를 우측, 하단으로 찾는다. -> 각각
    찾은 글자가 회문인지 판단한다.
    갯수를 센다.
    '''

    # times만큼 반복한다
    times = 8 - length + 1

    cnt = 0

    # 오른쪽으로 length글자
    # 오른쪽으로 찾기 때문에 행 방향으로는 끝까지 내려가도 됨.
    for i in range(8):
        for j in range(times):
            # arr[i][j]를 기준을 우측으로 찾는다
            right_word = ''
            # 글자에 += 으로 더해줌
            for k in range(length):
                right_word += arr[i][j+k]

            if right_word == right_word[::-1]:
                cnt += 1
                # print(right_word)
            # print(right_word)

    # 아래쪽으로 length글자
    for i in range(times):
        # 아래쪽으로 찾기 때문에 열 방향으로는 끝까지 가도 됨.
        for j in range(8):
            # arr[i][j]를 기준으로 아래쪽으로 찾는다
            down_word = ''
            # 글자에 += 으로 더해줌
            for k in range(length):
                down_word += arr[i + k][j]

            if down_word == down_word[::-1]:
                cnt += 1
                # print(down_word)

    print(f'#{test_case} {cnt}')