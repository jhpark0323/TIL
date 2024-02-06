import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    ls = input()

    # new_ls = []
    # for i in ls:
    #     new_idx = []
    #     if "'" in i:
    #         for j in i:
    #             if j == "'":
    #                 new_idx.append(i.index(j))
    #     new_word =

    # print(ls)
    stack = []
    answer = 1
    for i in ls:
        if i == "'" or i == '"':
            pass
            # 이부분 다시 해야함

        # i가 (, {이면 stack에 append
        if i in '({':
            stack.append(i)
        # i가 )이면 stack.pop으로 (가 나오는지 확인
        elif i == ')':
            if stack.pop() == '(':
                continue
            else:
                answer = 0
                break
        # i가 }이면 stack.pop으로 {가 나오는지 확인
        elif i == '}':
            if stack.pop() == '{':
                continue
            else:
                answer = 0
                break
        else:
            continue
    # stack의 길이가 0보다 크면 stack을 다 비우지 못했으므로 실패
    if len(stack) > 0:
        answer = 0

    print(f'#{test_case} {answer}')

# print("'", '"')