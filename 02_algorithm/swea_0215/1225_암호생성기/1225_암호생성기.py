import sys
sys.stdin = open('input.txt')

from collections import deque

# test_case의 갯수를 모름
while 1:
    try:
        # test_case
        T = int(input())
        # 암호배열
        ls = list(map(int, input().split()))
        # ls를 deque로 설정
        deq = deque(ls)
        # 맨마지막이 0이 될때 까지

        cycle = 1
        while deq[-1] != 0:
            # 맨앞의 원소를 뽑아서
            deq_pop = deq.popleft()
            # 맨뒤에 append 할 값
            deq_append = deq_pop - cycle
            # 0보다 작아지면 0으로 만듬
            if deq_append < 0:
                deq_append = 0

            # cycle만큼 빼서 뒤에 append
            deq.append(deq_append)

            if deq_append == 0:
                break

            # cycle을 주기를 가지고 더해줌
            cycle += 1

            # 만약 cycle이 6이되면 다시 1로 만들어줌
            if cycle == 6:
                cycle = 1

        print(f'#{T}', *deq)

    except EOFError:
        # 입력이 더 이상 없을 경우 종료
        break
