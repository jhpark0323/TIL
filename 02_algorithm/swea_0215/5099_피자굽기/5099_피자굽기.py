import sys
sys.stdin = open('sample_input.txt')

from collections import deque

T = int(input())

for test_case in range(1, T+1):

    n, m = map(int, input().split())
    ls = list(map(int, input().split()))

    # 화덕에는 n개의 피자를 동시에 구울 수 있다.
    deq = deque()
    for index, pizza in enumerate(ls):
        if len(deq) == n:
            # 계속 돌림
            while 1:
                # 첫번째 피자 빼서 치즈 반날리고 다시 뒤에 append
                pizza_pop = deq.popleft()
                # 반날리기
                pizza_pop[1] //= 2
                if pizza_pop[1] == 0:
                    break

                deq.append(pizza_pop)
                # print('pop', deq)
        if len(deq) < n:
            # 피자를 하나씩 빼서 deq에 삽입
            deq.append([index, pizza])
            # print('pizza ', deq)

    # for문이 끝나게 되면 deq에는 꽉차있는채로 끝남
    # 다시 한번 더 하는데 deq의 길이가 1이 되면 끝냄
    while 1:
        # 첫번째 피자 빼서 치즈 반날리고 다시 뒤에 append
        pizza_pop = deq.popleft()
        # 반날리기
        pizza_pop[1] //= 2
        if pizza_pop[1] == 0:
            pass
        else:
            deq.append(pizza_pop)
        if len(deq) == 1:
            answer = deq.pop()
            break
    # print(answer)
    print(f'#{test_case} {answer[0] + 1}')