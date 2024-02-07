import sys
sys.stdin = open('sample_input.txt')

def dfs(graph, start, end):
    stack = [start]
    visited = [False] * (len(graph))
    visited[start] = True
    # start가 방문한 곳들
    visited_start = []

    while stack:
        current_node = stack.pop()
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                visited_start.append(neighbor)

    if end in visited_start:
        answer = 1
    else:
        answer = 0
    return answer


T = int(input())

for test_case in range(1, T+1):
    # v개 이내의 노드를 e개의 간선으로 연결한 방향성 그래프
    v, e = map(int, input().split())

    # v개의 노드가 각각 갈수있는 graph
    graph = [[] for _ in range(v+1)]

    # e번 반복
    for i in range(e):
        # 각 노드별 시작과 끝점을 input값으로 받기
        start, end = map(int, input().split())
        # graph에 append
        graph[start].append(end)

    # 경로가 있는지 찾을 노드들(S, G)
    find_start, find_end = map(int, input().split())

    print(f'#{test_case} {dfs(graph, find_start, find_end)}')