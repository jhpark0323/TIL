import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def dijkstra():
    distance[0][0] = arr[0][0]
    pq = []

    # dist, 시작 index
    heappush(pq, (0, 0, 0))

    while pq:
        dist, current_row, current_col = heappop(pq)

        # 거리가 이미 저장된 누적거리보다 크면 볼필요 없음
        if dist > distance[current_row][current_col]:
            continue

        # 4방향을 돔
        for i in range(4):
            nxt_row = di[i] + current_row
            nxt_col = dj[i] + current_col

            # 범위 안에 있고
            if 0 <= nxt_row < n and 0 <= nxt_col < n:
                # 만약 다음 가는곳의 높이가 더 크면
                if arr[nxt_row][nxt_col] > arr[current_row][current_col]:
                    # nxt_dist는 거리의 차를 더해줌
                    nxt_dist = dist + arr[nxt_row][nxt_col] - arr[current_row][current_col] + 1
                # 다음 높이가 더 작으면
                else:
                    # 1만 더해줌
                    nxt_dist = dist + 1
                # 원래 저장된거 보다 더 짧으면
                if distance[nxt_row][nxt_col] > nxt_dist:
                    distance[nxt_row][nxt_col] = nxt_dist
                    heappush(pq, (nxt_dist, nxt_row, nxt_col))


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    inf = float('inf')

    # 누적 거리 저장
    distance = [[inf] * n for _ in range(n)]

    dijkstra()
    print(f'#{test_case} {distance[n-1][n-1]}')
