import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):

    k, n, m = map(int, input().split())

    bus_stop = list(map(int, input().split()))

    cnt = 1
    # 충전소 사이의 거리가 한번에 갈수있는 거리보다 길면 실패 -> cnt = 0 할당
    for i in range(1, len(bus_stop)):
        if (bus_stop[i] - bus_stop[i-1]) > k:
            cnt = 0


    # 첫번째 충전소 위치가 한번에 갈수있는 거리보다 길면 실패 -> cnt = 0 할당
    if bus_stop[0] > k:
        cnt = 0


    # 위의 두가지에 해당하지 않을 경우
    if cnt == 1:
        current = 0
        cnt = 0
        while 1:
            # 현재위치에 한번에 갈수있는 거리 할당
            current += k
            # if 현재위치가 버스정류장 길이보다 길면 끝
            if current >= n:
                break
            # bus_stop의 뒤부터 조사해서 current보다 작으면 그 정류장에서 충전
            for i in range(len(bus_stop)-1, -1, -1):
                if current >= bus_stop[i]:
                    # 현재위치를 충전한 버스정류장 위치로 변환
                    current = bus_stop[i]
                    cnt += 1
                    break

    print(f'#{test_case} {cnt}')