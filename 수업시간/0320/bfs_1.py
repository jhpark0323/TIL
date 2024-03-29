from collections import deque

# 인접 행렬 BFS
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
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
        for to in range(5):
            if graph[now][to] == 0:
                continue

            if visited[to]:
                continue

            visited[to] = 1
            print(visited)
            q.append(to)


bfs(0)