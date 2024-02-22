import sys
sys.stdin = open('s_input.txt')

T = int(input())

for test_case in range(1, T+1):
    # d : 거리, a : a기차 속력, b : b기차 속력, f : 파리의 속력
    d, a, b, f = map(int, input().split())
    # 기차 속력 합
    train_v_sum = a + b
    # 두 기차가 부딪힐 때 까지의 시간 : 거리 = 속력 x 시간
    time = d / train_v_sum
    # 파리가 움직일 수 있는 거리 : 속력 x 시간
    answer = f * time

    print(f'#{test_case} {answer}')