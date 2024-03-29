# 인접 행렬 DFS
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
]

visited = [0] * 5
path = []

def dfs(now):
    # 기저 조건
    # 지금 문제에선 없다!

    # 다음 재귀 호출 전
    # visited[now] = 1
    # path.append(now)
    # print(now, end = ' ')

    # 다음 재귀 호출
    # dfs: 현재 노드에서 다른 노드들을 확인
    # 다른 노드들 == 반복문
    for to in range(5):
        # 갈 수 없다면 pass
        if not graph[now][to]:
            continue

        # 이미 방문 했다면 pass
        if visited[to]:
            continue

        visited[to] = 1
        path.append(to)
        dfs(to)

    # 돌아왔을 때 작업

# 출발점 초기화
visited[0] = 1
path.append(0)
dfs(0)
print(path)