import sys
sys.stdin = open('input.txt')

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = int(input())

    ls = list(map(int, input().split()))

    total = 0

    # 비교해봐야 하는 건물의 갯수만큼 반복문 실행
    for i in range(2, n-2):
        highest = max(ls[i-1], ls[i-2], ls[i+1], ls[i+2])
        if ls[i] > highest:
            total += ls[i] - highest
    print(f'#{test_case} {total}')