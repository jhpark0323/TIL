import sys
sys.stdin = open('input.txt')

import decimal

def back(level, val):
    global max_val

    if max_val >= val:
        return

    if level == n:
        if max_val < val:
            max_val = val
        return

    for j in range(level, n):
        p[level], p[j] = p[j], p[level]
        back(level+1, val*0.01*arr[level][p[level]])
        p[level], p[j] = p[j], p[level]

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    p = [i for i in range(n)]

    max_val = -float('inf')
    back(0, 1)

    # answer = round(max_val*100, 7)
    answer = round(decimal.Decimal(max_val*100), 6)
    print(f'#{test_case} {answer}')