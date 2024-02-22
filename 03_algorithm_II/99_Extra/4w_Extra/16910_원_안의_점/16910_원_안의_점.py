import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    # 반지름
    r = float(input())

    cnt = 0
    # 반지름 만큼 순회
    for x in range(1, int(r+1)):
        for y in range(1, int(r+1)):
            if (x ** 2 + y ** 2) ** (1/2) <= r:
                cnt += 1
    # 축에 있는 점 들 -> 1 ~ r까지
    cnt += int(r)

    # 4개의 사분면 존재
    cnt *= 4

    # 원점
    cnt += 1

    print(f'#{test_case} {cnt}')