import sys
sys.stdin = open('sample_input.txt')

from collections import deque

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    ls = list(map(int, input().split()))

    idx = m % n
    print(f'#{test_case} {ls[idx]}')

