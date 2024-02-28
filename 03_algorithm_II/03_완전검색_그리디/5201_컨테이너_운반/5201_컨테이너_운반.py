import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    # n : 컨테이너 수, m : 트럭 수
    n, m = map(int, input().split())

    # 화물의 무게
    weight = list(map(int, input().split()))

    # 트럭의 적재용량
    truck = list(map(int, input().split()))

    weight.sort(reverse=True)
    truck.sort()

    print(n, m)
    print('화물의 무게 :', weight)
    print('트럭의 적재용량 :', truck)

    total = 0
    # 화물을 다 돌면 끝
    for i in range(n):
        now_weight = weight[i]

        if 0 <= i < m:
            now_truck = truck[-1]
        else:
            break

        # 화물이 트럭에 들어가면
        if now_truck >= now_weight:
            # total에 화물의 크기르 더한다
            total += weight[i]
            # 트럭을 뺌 -> 사용한 트럭
            truck.pop()
        # print(total)

    print(f'#{test_case} {total}')