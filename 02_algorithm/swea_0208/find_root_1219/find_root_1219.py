import sys
sys.stdin = open('input.txt')

'''
dfs를 이용해 0에서 부터 시작해 갈 수 있는 곳 전부 append
99가 그 list에 있으면 성공
'''

# start, end값이 고정이기에 굳이 매개변수로 받지 않음
def dfs(graph):
    # 방문한 곳 표시할 list -> 노드의 갯수만큼
    visited = [False] * 100
    stack = []
    # 빈 stack에 시작점 append
    stack.append(0)
    # 시작점은 방문
    visited[0] = True
    # 시작점으로부터 갈 수 있는 곳 apppend할 list
    can_go = []

    # stack이 빌때까지
    while stack:
        # 현재 노드는 stack의 제일 최근 값
        current_node = stack.pop()
        # graph에서 현재 노드로 부터 갈 수 있는 곳을 전부 조사
        for neighbor in graph[current_node]:
            # 방문하지 않은 곳이면
            if not visited[neighbor]:
                # 방문으로 변경
                visited[neighbor] = True
                # stack에 append
                stack.append(neighbor)
                # can_go에도 append
                can_go.append(neighbor)

    if 99 in can_go:
        answer = 1
    else:
        answer = 0
    return answer

# 테스트 케이스 10개 맞죠?
T = 10

for _ in range(T):
    test_case, length = map(int, input().split())

    ls = list(map(int, input().split()))

    # print(len(ls))

    # root에 방향을 append
    root = []
    for i in range(0, len(ls), 2):
        root.append((ls[i], ls[i+1]))
    # print(root)

    # 방향에 따라 graph를 만듬
    graph = [[] for _ in range(100)]
    for i in root:
        graph[i[0]].append(i[1])
    # print(graph)

    print(f'#{test_case} {dfs(graph)}')