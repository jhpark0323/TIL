import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    ls = input()

    # print(ls)
    stack = []
    answer = 1
    for i in ls:
        # ', "가 들어왔을 때
        if i == "'" or i == '"':
            # stack에 따옴표들이 안들어있을 때
            if i not in stack:
                # stack에 append
                stack.append(i)
            # stack에 들어있을 때
            else:
                while stack.pop() != i:
                    continue

        # i가 (, {이면 stack에 append
        elif i in '({':
            stack.append(i)
        # i가 )이면 stack.pop으로 (가 나오는지 확인
        elif i == ')':
            if (len(stack) > 0) and (stack.pop() == '('):
                continue
            else:
                answer = 0
                break
        # i가 }이면 stack.pop으로 {가 나오는지 확인
        elif i == '}':
            if (len(stack) > 0) and (stack.pop() == '{'):
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