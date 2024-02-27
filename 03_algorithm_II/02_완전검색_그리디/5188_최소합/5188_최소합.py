import sys
sys.stdin = open('sample_input.txt')

'''
branch는 갈수있는 방향 두개임
도착 index는 (n-1, n-1)
'''

def f(row, col, s):
    global min_s
    # 도착하면 종료
    if row == n-1 and col == n-1:
        if min_s > s:
            # print(path, sum(path))
            min_s = s
            # print(min_s)
        return

    elif min_s < s:
        return

    else:
        # branch를 돌며 움직임 -> dij
        for i in range(2):
            # 돌때 범위 안에 있으면
            if 0 <= row+di[i] < n and 0 <= col+dj[i] < n:
                # 지나온 경로에 append
                path.append(arr[row+di[i]][col+dj[i]])
                f(row+di[i], col+dj[i], s+arr[row+di[i]][col+dj[i]])
                path.pop()

# 갈수 있는 방향
di = [0, 1]
dj = [1, 0]

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    path = [arr[0][0]]
    cnt = 0
    min_s = float('inf')
    f(0, 0, arr[0][0])
    print(f'#{test_case} {min_s}')