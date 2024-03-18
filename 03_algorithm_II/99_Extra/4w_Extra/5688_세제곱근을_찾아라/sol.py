import sys
sys.stdin = open('input.txt')


T = int(input())

def func(l, r):
    if l > r:
        return -1
    m = (l + r) // 2
    if m**3 == N:
        return m
    elif m**3 > N:
        return func(l, m-1)
    elif m**3 < N:
        return func(m+1, r)


for tc in range(1, T+1):
    N = int(input())

    l, r = 1, N
    print(f'#{tc} {func(l, r)}')
