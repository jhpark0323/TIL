import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    bar = input()

    bar_ls = [*bar]
    stack = []
    # print(bar)
    # print(bar_ls)
    cnt = 0
    for i in range(len(bar_ls)):
        # 들어온게 (이면 stack에 append
        if bar_ls[i] == '(':
            stack.append(bar_ls[i])
        # 들어온게 )이면
        elif bar_ls[i] == ')':
            # 들어온 원소의 전 항이 (이면 그대로 pop해서 레이저로 만듬
            if bar_ls[i-1] == '(':
                stack.pop()
                # print(stack)
                # 이 때 stack에 남은 (갯수만큼 쇠막대기가 있을것이므로 그만큼 cnt에 추가 -> 잘린부분의 왼쪽 갯수
                cnt += len(stack)
            # 전 항이 )이면 쇠막대기의 끝부분임 -> 끝부분이 나오면 막대기가 끝났으므로 전에 레이저로 잘린부분의 오른쪽이 나옴 -> += 1
            else:
                stack.pop()
                cnt += 1

    print(f'#{test_case} {cnt}')