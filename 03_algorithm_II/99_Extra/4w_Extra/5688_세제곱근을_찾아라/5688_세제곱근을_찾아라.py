import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    # n의 세제곱근인데 파이썬이 보통 정확하게 못하는 경우가 있음
    # ex) 64**(1/3) -> 3.999999999996 뭐이런느낌

    cube_root = n ** (1/3)
    # print(n, cube_root)
    # print(cube_root ** 3)
    # print(int(cube_root))

    answer = -1

    # 그래서 걍 int때리거나
    if int(cube_root) ** 3 == n:
        answer = int(cube_root)

    # int때린거의 1큰수를 넣으면 보통 나옴
    elif(int(cube_root) + 1) ** 3 == n:
        answer = int(cube_root) + 1

    print(f'#{test_case} {answer}')