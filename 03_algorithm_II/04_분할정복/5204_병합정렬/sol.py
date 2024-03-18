import sys
sys.stdin = open('sample_input.txt')

from collections import deque

def merge_sort(m):
    if len(m) == 1:
        return m

    mid = len(m) // 2

    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global cnt
    result = []

    left = deque(left)
    right = deque(right)

    if left[-1] > right[-1]:
        cnt += 1

    while left or right:
        if left and right:
            if left[0] <= right[0]:
                result.append(left.popleft())

            else:
                result.append(right.popleft())

        elif left:
            result.append(left.popleft())

        elif right:
            result.append(right.popleft())

    return result

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    ai = list(map(int, input().split()))

    cnt = 0
    print(f'#{test_case} {merge_sort(ai)[n//2]} {cnt}')


