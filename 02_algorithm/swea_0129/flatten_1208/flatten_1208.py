import sys
sys.stdin = open('input.txt')

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dump = int(input())

    box = list(map(int, input().split()))

    # dump의 횟수 만큼 반복문 실행.
    for _ in range(dump):
        highest = max(box)
        lowest = min(box)
        box[box.index(highest)] -= 1
        box[box.index(lowest)] += 1
    print(f'#{test_case} {max(box) - min(box)}')