import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    code = input().split()
    # print(code)
    stack = []
    try:
        for char in code:
            # 숫자는 stack에 넣는다
            if char.isdigit():
                stack.append(char)
            # .을 만나면 출력한다
            elif char == '.':
                answer = stack.pop()
                # 비어있지 않다면 error
                if stack:
                    answer = 'error'
                break
            # 연산자를 만나면 stack의 두개를 꺼내 더하고 결과를 다시 stack에 넣음
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if char == '+':
                    result = first + second
                elif char == '-':
                    result = first - second
                elif char == '*':
                    result = first * second
                elif char == '/':
                    result = first // second
                else:
                    answer = 'error'
                    break
                stack.append(result)
    except:
        answer = 'error'

    print(f'#{test_case} {answer}')
