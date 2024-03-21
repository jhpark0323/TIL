import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop

def dijkstra():
    # 시작점
    distance[0] = 0
    # pq생성
    pq = []
    # 시작점 pq에 push
    # 누적거리, 시작점
    heappush(pq, (0, 0))

    while pq:
        dist, current = heappop(pq)

        # 현재 누적 거리가 가려는 거리보다 작으면 굳이 안해도 됨
        if distance[current] < dist:
            continue

        # 현재위치에서 갈 수 있는 곳
        for i in graph[current]:
            next_dist = dist + i[0]
            next_ = i[1]
            # print(next_dist, next_)

            # 현재 저장되어있는 누적 거리 보다 더 작은 값이 들어오면 갱신
            if 0 <= next_ <= n and distance[next_] > next_dist:
                distance[next_] = next_dist
                heappush(pq, (next_dist, next_))



T = int(input())

for test_case in range(1, T+1):
    n, e = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    for i in range(e):
        s, e, w = map(int, input().split())
        graph[s].append([w, e])
    # print(graph)

    inf = float('inf')
    distance = [inf] * (n+1)

    dijkstra()
    print(f'#{test_case} {distance[-1]}')
