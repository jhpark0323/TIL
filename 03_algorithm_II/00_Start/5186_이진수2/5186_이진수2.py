import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    # 십진수
    n = float(input())
    # 답을 담을 ls
    answer = []
    # -1 부터 -13까지 -1씩 증가
    for i in range(-1, -13, -1):
        # print(2**i)
        # n이 2**i보다 크면 계산
        if n >= 2 ** i:
            n -= 2 ** i
            # answer.append(2**i)

            # 계산 후 1 append
            answer.append('1')
        # 작으면 0 append
        else:
            answer.append('0')
        # 0이되면 끝
        if n == 0:
            break
    # for문을 다 돌았는데도 break가 안되면 0이 안되었다는 뜻
    else:
        answer = 'overflow'

    if type(answer) == list:
        answer = ''.join(answer)

    print(f'#{test_case} {answer}')