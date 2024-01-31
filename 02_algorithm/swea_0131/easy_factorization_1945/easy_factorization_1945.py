import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    n = int(input())

    # 각각의 지수에 대한 변수 지정
    exp_2 = 0
    exp_3 = 0
    exp_5 = 0
    exp_7 = 0
    exp_11 = 0

    # 소인수 분해가 되기 때문에 모든 과정을 진행하고 나면 n은 1이 될것임
    while n != 1:

        # n을 2로 나눴을때 나눠 떨어지면 exp_2에 1을 추가하고 n을 2로 나눈 몫을 다시 n에 할당
        if n % 2 == 0:
            exp_2 += 1
            n //= 2

        # n을 3으로 나눴을때 나눠 떨어지면 exp_3에 1을 추가하고 n을 3로 나눈 몫을 다시 n에 할당
        elif n % 3 == 0:
            exp_3 += 1
            n //= 3

        # n을 5로 나눴을때 나눠 떨어지면 exp_5에 1을 추가하고 n을 5로 나눈 몫을 다시 n에 할당
        elif n % 5 == 0:
            exp_5 += 1
            n //= 5

        # n을 7으로 나눴을때 나눠 떨어지면 exp_7에 1을 추가하고 n을 7로 나눈 몫을 다시 n에 할당
        elif n % 7 == 0:
            exp_7 += 1
            n //= 7

        # n을 11로 나눴을때 나눠 떨어지면 exp_11에 1을 추가하고 n을 11로 나눈 몫을 다시 n에 할당
        elif n % 11 == 0:
            exp_11 += 1
            n //= 11

    exponential = [exp_2, exp_3, exp_5, exp_7, exp_11]
    print(f'#{test_case}', *exponential)