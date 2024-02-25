def balloon_boom(row, col, k):
    s = 0
    for i in range(1, k+1):
        if 0 <= col+i < m:
            s += arr[row][col+i]
        if 0 <= col-i < m:
            s += arr[row][col-i]
        if 0 <= row+i < n:
            s += arr[row+i][col]
        if 0 <= row-i < n:
            s += arr[row-i][col]
    s += arr[row][col]
    return s



T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    max_s = 0
    for row in range(n):
        for col in range(m):
            s = balloon_boom(row, col, arr[row][col])
            if max_s < s:
                max_s = s

    print(max_s)