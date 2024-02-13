import sys
sys.stdin = open('input.txt')

# 후위 표기식으로 바꾸는 함수
def change(ls):
    stack = []
    postfix = ''
    for i in ls:
        # 숫자면 postfix에 += 해줌
        if i.isdigit():
            postfix += i
        # 연산자면 stack에 넣음
        if i == '+':
            if stack:
                postfix += stack.pop()
            stack.append(i)
    # 원래는 ()로 모든게 닫혀있는데 그게 없어서 마지막에 원소 하나가 남음
    # 그래서 걍 pop한번 더 해줌
    postfix += stack.pop()
    return postfix

# 후위 표기식 계산 함수
def calculate(postfix):
    stack = []
    for i in postfix:
        # 숫자면 stack에 append
        if i.isdigit():
            stack.append(int(i))
        # 연산자가 나오면 stack에서 두개 빼서 바로 계산
        elif i == '+':
            second = stack.pop()
            first = stack.pop()
            stack.append(first + second)

    return stack.pop()

T = 10

for test_case in range(1, T+1):
    length = int(input())

    ls = list(input())

    # print(change(ls))

    print(f'#{test_case} {calculate(change(ls))}')

