import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for x in range(100):
        stack = []
        for y in range(100):
            if arr[y][x] == 1 and not stack:
                stack.append(1)
            elif arr[y][x] == 2 and stack:
                result += stack.pop()
    print(f'#{tc} {result}')