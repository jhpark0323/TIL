import sys
sys.stdin = open('input.txt')

'''
시간초과인듯
'''

T = int(input())

for test_case in range(1, T+1):
    # m초후 k개를 만들수 있음
    n, m, k = map(int, input().split())
    # 손님이 도착하는 시간 list
    ls = list(map(int, input().split()))

    bungeo = 0
    time = 0
    people = 0
    length = len(ls)

    while 1:
        # 반복문이 돌 때 마다 1초씩 증가
        time += 1
        # 그 시간이 m으로 나눠떨어지면 붕어 k개 증가
        if time % m == 0:
            bungeo += k

        # ls에 그 시간에 오는 사람 수 체크
        people += ls.count(time)

        # 사람수가 붕어의 갯수보다 크면 실패
        if people > bungeo:
            answer = 'Impossible'
            break

        # 사람수가 ls의 길이와 같으면 모든 사람이 다온거임 성공!
        elif people == length:
            answer = 'Possible'
            break

    print(f'{test_case} {answer}')
