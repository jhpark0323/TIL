import sys
sys.stdin = open('sample_input.txt')

'''
왼쪽상단의 좌표를 기준으로 m만큼의 길이를 우측, 하단으로 찾는다. -> 각각
찾은 글자가 회문인지 판단한다.
'''

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())

    arr = [list(input()) for _ in range(n)]

    # times 만큼 반복
    times = n - m + 1

    # 오른쪽으로 m글자
    # 오른쪽으로 찾기 때문에 행 방향으로는 끝까지 내려가도 됨.
    for i in range(n):
        for j in range(times):
            # arr[i][j]를 기준을 우측으로 찾는다
            right_word = ''
            # 글자에 += 으로 더해줌
            for k in range(m):
                right_word += arr[i][j+k]

            if right_word == right_word[::-1]:
                answer = right_word

    # 아래쪽으로 m글자
    for i in range(times):
        # 아래쪽으로 찾기 때문에 열 방향으로는 끝까지 가도 됨.
        for j in range(n):
            # arr[i][j]를 기준으로 아래쪽으로 찾는다
            down_word = ''
            # 글자에 += 으로 더해줌
            for k in range(m):
                down_word += arr[i + k][j]

            if down_word == down_word[::-1]:
                answer = down_word
                # print(down_word)
    print(f'#{test_case} {answer}')