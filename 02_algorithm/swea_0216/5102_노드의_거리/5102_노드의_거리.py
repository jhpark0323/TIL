import sys
sys.stdin = open('sample_input.txt')

from collections import deque

def bfs(graph, start, n):
    global cnt
    visited = [0] * (n+1)
    visited[start] = 0
    q = deque()
    q.append(start)
    # q가 빌 때 까지
    while q:
        current_node = q.popleft()
        # 인접한 노드들을 큐에 추가
        # print(visited)
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                q.append(neighbor)
                # neighbor는 current_node에서 1만큼 더 움직임
                visited[neighbor] = visited[current_node] + 1
                if neighbor == g:
                    return visited[g]
    return visited[g]

T = int(input())

for test_case in range(1, T+1):
    # v : 노드의 갯수 e : 간선의 갯수
    v, e = map(int, input().split())

    ls = [list(map(int, input().split())) for _ in range(e)]
    # print(ls)

    # s : 출발노드, g : 도착노드
    s, g = map(int, input().split())

    # 빈 graph
    graph = [[] for _ in range(v+1)]

    # graph 만들기
    for i in ls:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    cnt = 0

    print(f'#{test_case} {bfs(graph, s, v)}')

