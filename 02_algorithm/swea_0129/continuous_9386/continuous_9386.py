import sys
sys.stdin = open('input1.txt')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    # 수열 a_n받기
    a_n = input()

    # max 초기값을 0으로 할당
    max_continuos = 0

    # 1이 연속으로 나오는 횟수의 초기값을 0으로 할당
    continuous = 0

    for i in range(n):
        # 수열의 i번째가 '1'일때
        if a_n[i] == '1':
            # continuous에 1씩 더해줌
            continuous += 1
            # max값 보다 continuous가 크면 max값에 continuous 할당
            if max_continuos < continuous:
                max_continuos = continuous
                # print(max_continuos)
        # 수열의 i번째가 '0'일때
        else:
            # 수열의 i-1번째가 1이면 continuous 0으로 초기화, 첫번째에 0이 들어가면 에러날 수 있으므로 i>=1 조건 추가
            if (int(a_n[i-1]) == 1) & (i >= 1):
                continuous = 0

    print(f'#{test_case} {max_continuos}')