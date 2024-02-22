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

    answer = 0

    # 전부 다 순회
    # first는 처음꺼 부터 마지막 전까지
    for i in range(n-1):
        for j in range(i+1, n):
            # 첫번째 두번째 전봇대
            first, second = arr[i], arr[j]
            # 둘이 빼서 곱했을 때 음수이면 겹침
            if (first[0] - second[0]) * (first[1] - second[1]) < 0:
                answer += 1

    print(f'#{test_case} {answer}')