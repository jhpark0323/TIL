# import sys
# sys.stdin = open('input.txt')
#
# def back(level, val):
#     global min_val
#     if level == n:
#         if min_val > val:
#             min_val = val
#         return
#
#     if min_val <= val:
#         return
#
#     for j in range(level, n):
#         p[level], p[j] = p[j], p[level]
#         back(level+1, val+arr[level][p[level]])
#         p[level], p[j] = p[j], p[level]
#
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     p = [i for i in range(n)]
#
#     min_val = float('inf')
#     back(0, 0)
#     print(f'#{test_case} {min_val}')
#



import sys
sys.stdin = open('input.txt')

def back(level, val):
    global min_val
    if level == n:
        if min_val > val:
            min_val = val
        print(p)
        return

    if min_val <= val:
        return

    for j in range(level, n):
        p[level], p[j] = p[j], p[level]
        back(level+1, val+arr[level][p[level]])
        p[level], p[j] = p[j], p[level]


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    p = [i for i in range(n)]

    min_val = float('inf')
    back(0, 0)
    print(f'#{test_case} {min_val}')