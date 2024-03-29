'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

from heapq import heappush, heappop

# 큰값
INF = float('inf')

V, E = map(int, input().split())
# 시작 노드 번호
start = 0

# 인접 ls
graph = [[] for _ in range(V)]

# 누적거리를 저장할 변수
distanse = [INF] * V

# 간선 정보 저장
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])
print(graph)
def dijkstra(start):
    pq = []

    # 시작점의 weight, node 번호를 한번에 저장
    heappush(pq, (0, start))
    # 시작 노드 초기화
    distanse[start] = 0

    while pq:
        # 최단 거리 노드에 대한 정보
        dist, now = heappop(pq)

        # pq의 특성 떄문에 더 긴거리가 미리 저장되어 있음
        # now가 이미 더 짧은 거리로 온 적이 있다면 pass
        if distanse[now] < dist:
            continue

        # now에서 인접한 다른 노드 확인
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]

            # 누적 거리 계산
            new_dist = dist + next_dist

            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distanse[next_node]:
                continue

            # 누적 거리를 최단거리로 갱신
            distanse[next_node] = new_dist
            # next_node의 인접 노드들을pq에 추가
            heappush(pq, (new_dist, next_node))

dijkstra(0)
print(distanse)