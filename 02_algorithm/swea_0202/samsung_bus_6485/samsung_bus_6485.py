import sys
sys.stdin = open('s_input.txt')

T = int(input())

for test_case in range(1, T+1):

    n = int(input())

    # 문제가 머라는지를 모르겠네;

    # i번째 노선의 시작정류장(ai)과 끝정류장(bi) -> ai와 bi 사이의 모든 정류장을 다님
    ai_bi = [list(map(int, input().split())) for _ in range(n)]

    # p개의 정류장에 대해
    p = int(input())

    # 각 정류장에 몇개의 버스노선이 다니나요?
    each_bus_stop = [int(input()) for _ in range(p)]

    # print(n)
    # print(ai_bi)
    # print(p)
    # print(each_bus_stop)

    # 버스정류장은 0 ~ 5001까지 둠 -> 이래야 index 구할때 편할듯
    bus_stop = [0] * 5001

    # 각 ai_bi에서 0번째 index를 시작, 1번째 index를 끝으로 둠
    for start_end in ai_bi:
        ai, bi = start_end[0], start_end[1]
        # ai부터 bi까지 하나씩 더해줄거임
        for plus in range(ai, bi+1):
            bus_stop[plus] += 1

    # 답을 받을 ls
    answer = []

    # each_bus_stop에서 각각의 원소를 반복해 그 원소를 index로 하는 bus_stop의 원소를 answer에 append
    for i in each_bus_stop:
        answer.append(bus_stop[i])

    print(f'#{test_case}', *answer)