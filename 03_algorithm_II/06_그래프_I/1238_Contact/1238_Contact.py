import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start):
    visited = [0 for _ in range(101)]
    visited[start] = 1
    q = deque([[start, 0]])

    while q:
        current, cnt = q.popleft()

        for neighbor in graph[current]:
            # 방문하지 않았다면
            if not visited[neighbor]:
                q.append([neighbor, cnt+1])
                cnt_ls.append([neighbor, cnt+1])
                visited[neighbor] = 1

    return cnt



for test_case in range(1, 11):
    n, start = map(int, input().split())
    ls = list(map(int, input().split()))

    # 인원은 1부터 100까지
    graph = [[] for _ in range(101)]
    # print(graph)

    # 처음부터 2개씩
    for i in range(0, n, 2):
        graph[ls[i]].append(ls[i+1])
    # print(graph)

    cnt_ls = [[start, 0]]
    max_cnt = bfs(start)
    # print(cnt_ls)
    # print(max_cnt)

    ans_ls = []
    while 1:
        now = cnt_ls.pop()
        if now[1] == max_cnt:
            ans_ls.append(now[0])

        if now[1] != max_cnt:
            break

    print(f'#{test_case} {max(ans_ls)}')