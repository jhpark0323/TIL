import sys
sys.stdin = open('input.txt')

T = int(input())
'''
재현아... 이 문제는 너무 어렵게 생각하지마...ㅎ
그냥 다 비교해... 시간초과 안뜨더라,,,,하핳
'''

for test_case in range(1, T+1):
    # n개의 팽팽한 전선
    n = int(input())
    # i번째 전선이 j(1 or2)번째 전봇대의 arr[i][j]의 높이에 있음
    arr = [list(map(int, input().split())) for _ in range(n)]

    ls = [-1 for _ in range(10001)]
    # arr을 순회하며 전선을 찾음
    for i in range(n):
        # 전선줄
        elec_line = arr[i]
        # 첫번째 가로등 높이, 두번째 가로등 높이
        first, second = elec_line[0], elec_line[1]
        # print(first, second)

        # 1씩 더해줌
        if first <= second:
            for j in range(first, second+1):
                ls[j] += 1
                # print(ls[j])
        else:
            for j in range(second, first+1)
    # print(ls)

    # ls에 0보다 큰 수가 들어있으면 더하기
    answer = 0
    # for i in ls:
    #     if i > 0:
    #         answer += i

    print(f'#{test_case} {answer}')