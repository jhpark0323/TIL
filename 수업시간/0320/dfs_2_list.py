# 인접 list DFS
graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3],
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
    # 인접 list
    # 차이점 1. 갈 수 없는 곳 조건 필요 없음
    # 차이점 2. for 문 작성 수정
    for to in graph[now]:
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