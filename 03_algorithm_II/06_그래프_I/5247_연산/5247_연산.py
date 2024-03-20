import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs():
    # visited = set()
    # visited.add(n)
    visited = [0] * 1000001
    visited[n] = 1

    q = deque([[n, 0]])

    while q:
        current, cnt = q.popleft()

        # 기저 조건
        if current == m:
            return cnt

        # 4번의 연산을 돌릴때
        for next in [current+1, current-1, current*2, current-10]:
            # 방문한적이 없고 백만이하의 자연수이면
            # if 0 < next <= 1000000 and next not in visited:
            if 0 < next <= 1000000 and not visited[next]:
                q.append([next, cnt+1])
                # visited.add(next)
                visited[next] = 1

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())

    count = bfs()
    print(f'#{test_case} {count}')