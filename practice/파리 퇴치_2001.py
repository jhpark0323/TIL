def fly_catch(i, j):
    s = 0
    for ii in range(m):
        for jj in range(m):
            s += arr[i + ii][j + jj]
    return s

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    max_s = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            s = fly_catch(i, j)
            if max_s < s:
                max_s = s

    print(f'#{test_case} {max_s}')