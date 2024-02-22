import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    ls = list(input().split())
    # print(ls)

    # ls길이가 짝수면
    if n % 2 == 0:
        first_ls = ls[:n//2]
        second_ls = ls[n//2:]
    # ls길이가 홀수면
    else:
        first_ls = ls[:n//2+1]
        second_ls = ls[n//2+1:]
    # print(first_ls, second_ls)

    # 새로운 ls에 각각을 차례로 append
    new_ls = []
    for i in range(n//2):
        new_ls.append(first_ls[i])
        new_ls.append(second_ls[i])
    # 홀수개여서 하나가 남으면 마지막에 하나 더 append
    if n % 2 == 1:
        new_ls.append(first_ls.pop())
    print(f'#{test_case}', *new_ls)