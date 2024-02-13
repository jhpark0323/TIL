import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T+1):
    length = int(input())

    string = input()


    # 우선순위
    icp = {
        '+' : 1,
        '*' : 2
    }

    postfix = ''
    stack = []
    # 후위 표기식으로 바꾸기
    for i in string:
        # 숫자면 postfix에 추가
        if i.isdigit():
            postfix += i

        # stack이 비어있으면 append
        elif not stack:
            stack.append(i)

        # 연산자이고 맨위 원소보다 우선순위가 높으면 push
        elif i in '+*' and icp[stack[-1]] < icp[i]:
            stack.append(i)

        # 연산자이고 맨위 원소보다 우선순위가 높지 않으면 pop
        elif i in '+*' and icp[stack[-1]] >= icp[i]:
            # 맨위의 원소가 우선순위가 낮아질때 까지
            while stack and icp[stack[-1]] > icp[i]:
                postfix += stack.pop()
            # *다 빼고 + 만나면 while문 종료 후 stack이 남아있으면 +하나 postfix에 넣기
            if stack:
                postfix += stack.pop()
            # 다 하고 난 후 연산자 append
            stack.append(i)
    while stack:
        postfix += stack.pop()
    # print(postfix)
    # print(stack)

    # 계산하기
    number = []
    for i in postfix:
        # 숫자면 number에 append
        if i.isdigit():
            number.append(i)

        # 연산자면 두개 뺴서 계산
        else:
            second = int(number.pop())
            first = int(number.pop())
            if i == '+':
                number.append(first+second)
            elif i == '*':
                number.append(first*second)
    print(f'#{test_case} {number[0]}')