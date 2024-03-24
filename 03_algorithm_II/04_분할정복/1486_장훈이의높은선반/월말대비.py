import sys
sys.stdin = open('input.txt')

def f(cnt, height):
# def f(cnt, height, visited):
    global answer

    # 기저 조건
    # b는 항상 hi의 합보다 작으므로 무조건 답은 나온다.
    # 합이 b이상이면 그만
    if height >= b:
        # answer가 height보다 크면 answer = height
        if answer > height:
            answer = height
        return

    if cnt == n:
        return

    f(cnt + 1, height + hi[cnt])
    f(cnt + 1, height)

    # for i in range(n):
    #     if not visited[i]:
    #         visited[i] = 1
    #         f(cnt+1, height + hi[i], visited)
    #         visited[i] = 0

T = int(input())

for test_case in range(1, T+1):
    n, b = map(int, input().split())
    hi = list(map(int, input().split()))
    answer = float('inf')
    visited = [0] * n

    # f(0, 0, visited)
    f(0, 0)

    print(f'#{test_case} {answer - b}')