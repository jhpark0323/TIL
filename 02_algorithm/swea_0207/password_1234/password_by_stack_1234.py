import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T+1):
    n, pw = input().split()
    n = int(n)

    stack = []

    # pw의 각 글자에 접근
    for i in pw:
        # stack이 비었으면 i를 append
        if len(stack) == 0:
            stack.append(i)

        # stack의 마지막 원소와 i가 다르면 append
        elif stack[-1] != i:
            stack.append(i)

        # stack의 마지막 원소와 i가 같으면 pop
        elif stack[-1] == i:
            stack.pop()

    print(f"#{test_case} {''.join(stack)}")