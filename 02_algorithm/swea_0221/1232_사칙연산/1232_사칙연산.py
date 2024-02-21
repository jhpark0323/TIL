import sys
sys.stdin = open('input.txt')

# 후위 순회
def post_order(t):
    # global answer
    if t:
        post_order(left[t])
        post_order(right[t])
        # arr에서 1번째 값이 트리안의 원소임
        # print(arr[t-1][1], end = ' ')
        # answer += str(arr[t-1][1]) + ' '
        ls.append((arr[t-1][1]))

# 계산
def cal(k):
    # 숫자면 stack에 append
    if isinstance(k, int):
        stack.append(k)
    # 연산자면 계산
    else:
        second = stack.pop()
        first = stack.pop()
        if k == '+':
            stack.append(first+second)
        elif k == '-':
            stack.append(first - second)
        elif k == '*':
            stack.append(first*second)
        elif k == '/':
            stack.append(first/second)


for test_case in range(1, 11):
    # 정점의 갯수
    n = int(input())
    # 트리 받아오기
    arr = []
    for i in range(n):
        a = list(input().split())
        for j in range(len(a)):
            if a[j].isdigit():
                a[j] = int(a[j])
        arr.append(a)
    # print(arr)

    left = [0] * (n+1)
    right = [0] * (n+1)

    # 왼쪽 오른쪽 자식 트리 만들기
    for i in range(n):
        # 길이가 4이면 연산자임 -> 좌우 자식이 다있음
        if len(arr[i]) == 4:
            parent = arr[i][0]
            left_child = arr[i][2]
            right_child = arr[i][3]
            left[parent] = left_child
            right[parent] = right_child

    # 연산자 계산하기
    # 빈 ls
    ls = []
    post_order(1)
    print(ls)

    # 빈 stack 생성
    stack = []

    for i in ls:
        cal(i)

    # print(ls)
    print(f'#{test_case}', int(stack.pop()))