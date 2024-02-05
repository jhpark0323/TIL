import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    # 파스칼 삼각형 담을 list 생성
    p_tri = []

    # n만큼 반복
    for line in range(n):
        # 첫줄은 무조건 1
        ls = [1]
        if line == 0:
            p_tri.append(ls)

        # 둘째줄부터
        else:
            # ls에 index1부터 line까지 반복
            for j in range(1, line):
                if j >= 0:
                # p_tri의 마지막 list에서 j-1번째, j번째 index의 합 ls에 append
                    ls.append(p_tri[-1][j-1] + p_tri[-1][j])

            ls.append(1)
            p_tri.append(ls)

    print(f'#{test_case}')
    for i in range(n):
        print(*p_tri[i])
