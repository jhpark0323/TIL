import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    n = len(str1)
    m = len(str2)

    # max_cnt에 최댓값 대입
    max_cnt = 0
    for i in str1:
        cnt = str2.count(i)
        if max_cnt < cnt:
            max_cnt = cnt
            # print(i)
    print(f'#{test_case} {max_cnt}')