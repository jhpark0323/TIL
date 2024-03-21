import sys
sys.stdin = open('input.txt')

from pprint import pprint
from heapq import heappush, heappop

def prim():
    # priority queue
    pq = []
    # 방문한 노드표시
    visited = [0] * (v+1)
    # 가중치
    sum_cost = 0
    # 시작점 0, 가중치 0
    heappush(pq, (0, 0))

    while pq:
        # print(pq)
        # 시작노드, 비용 뽑기
        cost, current = heappop(pq)
        # print(current, cost)

        # pq의 특성상 최소값부터 방문하는거라 pq의 뒤에 또 남아있을 수 있음
        # 그 부분 제거
        if visited[current]:
            continue

        # 방문표시는 여기서 함
        visited[current] = 1

        sum_cost += cost
        # print(current, cost)

        # 연결된 graph 순회
        for neighbor in range(v+1):
            # 연결된 곳이 갈 수 있고 (0이아니고) 방문하지 않았다면
            if graph[current][neighbor] and not visited[neighbor]:
                # pq에 연결된 곳의 위치와 그때의 가중치를 더해줌
                heappush(pq, (graph[current][neighbor], neighbor))

    # print(sum_cost)
    return sum_cost

T = int(input())

for test_case in range(1, T+1):
    v, e = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(e)]

    graph = [[0] * (v+1) for _ in range(v+1)]

    for i in range(e):
        start, end, weight = arr[i][0], arr[i][1], arr[i][2]
        graph[start][end] = weight
        graph[end][start] = weight
    # pprint(graph)

    ans = prim()
    print(f'#{test_case} {ans}')