import sys
sys.stdin = open('sample_input.txt')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n, m = map(int,input().split())

    ls = list(map(int, input().split()))
    # total_ls에 빈 list를 할당 -> 구간합들을 담을 예정
    total_ls = []
    # n개중 m으로 묶은 구간합의 갯수
    for i in range(n-m+1):
        total = 0
        # m번 반복하여 m개의 구간합 구하기
        for j in range(m):
            total += ls[i+j]
        total_ls.append((total))

    print(f'#{test_case} {max(total_ls) - min(total_ls)}')