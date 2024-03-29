from collections import deque

# 인접 list BFS
graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3],
]

def bfs(start):
    visited = [0]*5

    # 시작노드를 큐에 추가 + 방문 표시
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()
        print(now, end=' ')

        # 갈 수 있는 곳을 체크
        for to in graph[now]:
            if visited[to]:
                continue

            visited[to] = 1
            # print(visited)
            q.append(to)

bfs(0)