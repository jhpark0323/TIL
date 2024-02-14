import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 복도 총 201개
    corridor = [0] * 201
    # 각 arr에서
    for stu_room in arr:
        # 학생이 지나간 복도를 전부 1씩 증가 시켜줌
        # 복도에 따른 index 조정
        if stu_room[0] % 2 == 0:
            stu_room[0] //= 2
        else:
            stu_room[0] = stu_room[0] // 2 + 1

        if stu_room[1] % 2 == 0:
            stu_room[1] //= 2
        else:
            stu_room[1] = stu_room[1] // 2 + 1

        # 시작을 더작은 값, 끝을 더 큰값으로 설정
        start = min(stu_room[0], stu_room[1])
        end = max(stu_room[0], stu_room[1])
        for i in range(start, end+1):
            corridor[i] += 1
    # 복도의 최댓값이 결국 필요한정도
    print(f'#{test_case} {max(corridor)}')
